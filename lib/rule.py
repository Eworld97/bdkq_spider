# coding: utf-8

import sys

from lib.log_helper import get_logger

LOG = get_logger("task")


def filter_rule_settings(rule_settings):
    """过滤掉SETTINGS中的空白字段

    :type rule_settings: dict
    :return: rule_settings without blank fields
    :type: dict
    """

    try:
        return dict(filter(lambda key_value: len(key_value[1]) > 0, rule_settings.items()))
    except Exception as e:
        LOG.error("[lib task] wrong field type in task_conf.py, please check the config! error: {}".format(e))
        return dict()


class Rule(object):
    field_func_mapping_table = {
        "sorts": "positive_selection",
        "department": "positive_selection",
        "time": "positive_selection",
        "week": "positive_selection",
        "doctor": "positive_selection",
        "title": "positive_selection",
        "doctor_reverse": "invert_selection",
        "title_reverse": "invert_selection",
    }

    def __init__(self, rule_settings):
        """根据rule_settings各字段的设置返回rule实例，lib.parser会根据rule list匹配票号

        :param rule_settings:
        """
        self.__sorts = rule_settings.get("sorts", None)
        if not self.__sorts:
            LOG.error("[lib task] 挂号种类字段必须填写！！!")
            sys.exit()

        self.__department = rule_settings.get("department", None)
        self.__time = rule_settings.get("time", None)
        self.__week = rule_settings.get("week", None)
        self.__title = rule_settings.get("title", None)
        self.__title_reverse = rule_settings.get("title_reverse", None)
        self.__doctor = rule_settings.get("doctor", None)
        self.__doctor_reverse = rule_settings.get("doctor_reverse", None)

        self.__rule_list = []
        self.patch_rule_list()

    def patch_rule_list(self):
        self.__rule_list.append("sorts")
        if self.__department:
            self.__rule_list.append("department")
        if self.__time:
            self.__rule_list.append("time")
        if self.__week:
            self.__rule_list.append("week")
        if self.__doctor:
            self.__rule_list.append("doctor")
        elif self.__doctor_reverse:
            self.__rule_list.append("doctor_reverse")
        if self.__title:
            self.__rule_list.append("title")
        if self.__title_reverse:
            self.__rule_list.append("title_reverse")

    @property
    def rule_list(self):
        return self.__rule_list

    @property
    def sorts(self):
        return self.__sorts

    @property
    def department(self):
        return self.__department

    @property
    def time(self):
        return self.__time

    @property
    def week(self):
        return self.__week

    @property
    def title(self):
        return self.__title

    @property
    def title_reverse(self):
        return self.__title_reverse

    @property
    def doctor(self):
        return self.__doctor

    @property
    def doctor_reverse(self):
        return self.__doctor_reverse

    @staticmethod
    def invert_selection(text, select_list):
        """反向选择
        select_list为选择列表，当选择列表里每个字段都不与text匹配时返回true，任一字段能匹配上则返回false

        :param text:
        :param select_list:
        :rtype: bool
        """

        for s in select_list:
            if s in text:
                return False
        return True

    @staticmethod
    def positive_selection(text, select_list):
        """正向选择
        select_list为选择列表，当选择列表里任一字段与text匹配时返回true，无一匹配返回false

        :param text:
        :param select_list:
        :rtype: bool
        """

        for s in select_list:
            if s in text:
                return True
        return False
