# coding: utf-8

import sys

from bs4 import BeautifulSoup

from etc.config import EXIT_WHEN_PARSE_EXCEPTION
from lib.email_helper import send_email
from lib.log_helper import get_logger

LOG = get_logger("html_parser")


def parse_response(html_text, rule):
    """

    :param html_text: text/html (bytes or unicode)
    :param rule: instance of lib.rule.Rule
    :rtype: bool
    """
    try:
        soup = BeautifulSoup(html_text, "html.parser")
    except Exception as e:
        LOG.error("[html parser] error: {}".format(e))
        if EXIT_WHEN_PARSE_EXCEPTION:
            sys.exit()
        return False

    # 根据class标签匹配所有剩余票号
    element_set = soup.find_all("div", attrs={'class': ['rbk-listitem', 'rbk-table-view-cell']})
    if not element_set:
        LOG.warning("[html parser] Cannot parse out any elements, check the css selector !")
        return False

    res = match_the_tickets(element_set, rule)
    if res:
        LOG.warning("[html parser] Found tickets left !")
        LOG.warning(res)
        send_email(str(res))
        return True
    LOG.info("[html parser] No tickets found ! Continue crawling...")
    return False


def match_the_tickets(element_set, rule):
    """遍历rule对象的rule_list, 找到符合要求的票号.

    :param element_set: A ResultSet of PageElements
    :param rule: instance of lib.rule.Rule
    :rtype: str
    """

    rule_field_list = rule.rule_list
    tickets_info = ""

    for element in element_set:
        # 每一个element为一条剩余号源的记录(含html标签)
        trans_map = {ord("\r"): None, ord("\t"): None, ord("\n"): " "}
        text = element.text.translate(trans_map)

        _continue = False
        # 遍历找票规则, 一条条筛选
        for field in rule_field_list:
            select_func = getattr(rule, rule.field_func_mapping_table.get(field))
            if not select_func(text, getattr(rule, field)):
                _continue = True
                break
        if _continue:
            continue

        # 所有规则都满足，则追加该次查询记录
        tickets_info = "{}\n{}".format(tickets_info, text)

    return tickets_info
