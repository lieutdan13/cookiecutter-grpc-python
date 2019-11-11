import logging
import os


LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()


def module_logger(module_name):

    logger = logging.Logger(module_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(LOGLEVEL)

    return logger
