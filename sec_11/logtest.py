import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# FileHandlerの設定、loggerへの追加
h = logging.FileHandler('logtest.log')
logger.addHandler(h)


def do_something():
    # ここでloggingを使用すると呼び出し元の設定を用いてしまう
    # logging.info('from logtest info')
    logger.info('from logtest')
    logger.debug('from logtest debug')
