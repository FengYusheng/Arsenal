# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler


def build_logger(module_name=None):
    """
    logger, handler, filter, formatter
    :param module_name:
    :return: logger
    """
    formatter_ = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler_ = RotatingFileHandler('./logs/requestman.log', mode='a', maxBytes=3*1024*1024, encoding='utf-8', backupCount=10, delay=0)
    handler_.setFormatter(formatter_)
    logger = logging.getLogger(module_name)
    logger.addHandler(handler_)
    logger.setLevel(logging.DEBUG)

    return logger


__all__ = [
    'build_logger'
]