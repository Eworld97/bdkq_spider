# -*- coding: utf-8 -*-

import os

# Host settings
BDKQ_HOST = "bdkqyy.zwjk.com"

# API settings
TICKETS_LEFT_API = "https://{}/hospital/leftno.htm".format(BDKQ_HOST)

# email settings
MAIL_HOST = "smtp.126.com"
MAIL_PORT = 25
MAIL_SENDER_USERNAME = os.environ.get("MAIL_SENDER_USERNAME", "")
MAIL_SENDER_AUTH_KEY = os.environ.get("MAIL_SENDER_AUTH_KEY", "")
MAIL_RECEIVER_USERNAME = os.environ.get("MAIL_RECEIVER_USERNAME", "")

# log settings
LOG_LEVEL_DEFAULT = os.environ.get("LOG_LEVEL", "INFO")

# request settings
TLS_VERIFY = False
TLS_WARNING = False

API_TIMEOUT = (8, 8)

SLEEPING_TIME_WHEN_SUCCESS = 60
NORMAL_SLEEPING_TIME = 10

EXIT_WHEN_WHEN_SUCCESS = False

# handle exception settings
EXIT_WHEN_PARSE_EXCEPTION = True
EXIT_WHEN_REQUEST_EXCEPTION = True

