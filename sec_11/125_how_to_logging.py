import logging

logger = logging.getLogger(__name__)

logger.error('Api call is failed')

# key-value で書くと解析が楽になる（主に解析ソフト向け）
logger.error({
    'action': 'create',
    'status': 'fall',
    'message': 'Api call is failed'
})
