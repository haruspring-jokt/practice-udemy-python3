import logging

import logtest

logging.basicConfig(level=logging.INFO)


class NoPassFilter(logging.Filter):
    def filter(self, record):
        """

        :param record:
        :return: 'password'が含まれている場合はFalseを返す
        """
        log_message = record.getMessage()
        return 'password' not in log_message


# logger = logging.getLogger(__name__)
# logger.info('from main')

# logtest.do_something()

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
# NoPassFilterを追加したので、'password'が含まれたログは出力されない
logger.info('from main password = "test"')
