# coding: utf-8

import time
import sys
import urllib3

import requests
from requests.exceptions import RequestException

from etc.config import (
    API_TIMEOUT,
    EXIT_WHEN_REQUEST_EXCEPTION,
    EXIT_WHEN_WHEN_SUCCESS,
    NORMAL_SLEEPING_TIME,
    SLEEPING_TIME_WHEN_SUCCESS,
    TICKETS_LEFT_API,
    TLS_VERIFY,
    TLS_WARNING,
)
from etc.rule_settings import SETTINGS
from lib.log_helper import get_logger
from lib.parser import parse_response
from lib.rule import Rule, filter_rule_settings

LOG = get_logger("daemon")

if not TLS_WARNING:
    urllib3.disable_warnings()


def main():
    rule_settings = filter_rule_settings(SETTINGS)
    rule = Rule(rule_settings)

    while True:
        try:
            res = requests.get(TICKETS_LEFT_API, verify=TLS_VERIFY, timeout=API_TIMEOUT)
        except RequestException as e:
            LOG.error("[API request] error: {}".format(e))
            if EXIT_WHEN_REQUEST_EXCEPTION:
                sys.exit()
            continue

        status = parse_response(res.content, rule)
        if status:
            if EXIT_WHEN_WHEN_SUCCESS:
                sys.exit()
            time.sleep(SLEEPING_TIME_WHEN_SUCCESS)
        else:
            time.sleep(NORMAL_SLEEPING_TIME)


if __name__ == '__main__':
    main()
