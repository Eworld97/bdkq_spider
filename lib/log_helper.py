# -*- coding: utf-8 -*-


import logging

from colorlog import ColoredFormatter

from etc.config import LOG_LEVEL_DEFAULT

# color formatter
HANDLER = logging.StreamHandler()
FORMATTER = ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s%(asctime)s %(message_log_color)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={
        'message': {
            'ERROR': 'red',
            'CRITICAL': 'red'
        }
    },
    style='%'
)
HANDLER.setFormatter(FORMATTER)


def get_logger(logger_name, level=LOG_LEVEL_DEFAULT):
    logger = logging.getLogger(logger_name)
    logger.addHandler(HANDLER)
    logger.setLevel(level)
    return logger
