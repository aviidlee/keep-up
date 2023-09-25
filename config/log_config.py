import logging
from logging import Logger

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')


def logger(name: str) -> Logger:
    return logging.getLogger(name)
