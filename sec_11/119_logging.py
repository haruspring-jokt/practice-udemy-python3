import logging

# デフォルトのレベルはwarningだが、変更できる
logging.basicConfig(filename='test.log', level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

# x = 10

logging.info(f'info %s' % 'test')
