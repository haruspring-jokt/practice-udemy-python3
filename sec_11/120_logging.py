import logging

# デフォルトのレベルはwarningだが、変更できる
# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatter)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# x = 10

logging.info('info %s %s', 'test', 'test2')
