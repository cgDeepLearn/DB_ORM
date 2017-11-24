# -*- coding: utf8 -*-
import os
import logging
import logging.config
from config import BASE_DIR


conf_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logger.cfg')
log_dir = BASE_DIR + '/logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_path = os.path.join(log_dir, 'test.log')

# 使用fileConfig
#logging.config.fileConfig(conf_name)
# 坑爹的qualname

#使用dictConfig
myconfig_dict = {
    'version': 1.0,
    'formatters': {
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detail'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': log_path,
            'level': 'INFO',
            'formatter': 'detail',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'crawler': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'parser': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'other': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'storage': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    }
}

logging.config.dictConfig(myconfig_dict)

crawler = logging.getLogger('crawler')
parser = logging.getLogger('parser')
other = logging.getLogger('other')
#other = logging.getLogger('root')
storage = logging.getLogger('storage')

