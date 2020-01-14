# -*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText

from etc.config import (
    MAIL_HOST,
    MAIL_PORT,
    MAIL_SENDER_USERNAME,
    MAIL_SENDER_AUTH_KEY,
    MAIL_RECEIVER_USERNAME,
)
from lib.log_helper import get_logger

LOG = get_logger("email")


def send_email(content):
    """
    默认使用126smtp, etc/config中修改

    :param content: email content
    :return:
    """

    msg = MIMEText(content)
    msg['Subject'] = "[抢票器] 发现剩余号源"  # title
    msg['From'] = MAIL_SENDER_USERNAME
    msg['To'] = MAIL_RECEIVER_USERNAME
    smtp = None
    try:
        smtp = smtplib.SMTP(MAIL_HOST, port=MAIL_PORT)
        smtp.login(MAIL_SENDER_USERNAME, MAIL_SENDER_AUTH_KEY)  # need auth_key ,not password
        smtp.sendmail(MAIL_SENDER_USERNAME, MAIL_RECEIVER_USERNAME, msg.as_string())
    except Exception as e:
        LOG.error("[bdkq email] error: {}".format(e))
    finally:
        if smtp:
            smtp.quit()


def disable_mail(content):
    return


if MAIL_SENDER_USERNAME and MAIL_SENDER_AUTH_KEY and MAIL_RECEIVER_USERNAME:
    LOG.info("[bdkq email] Email notification is on.")
else:
    send_email = disable_mail
    LOG.warn("[bdkq email] Email notification is off !!!")
