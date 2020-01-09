from typing import Any, Dict, Union

import os


LOGGING: Dict[str, Union[Dict[str, Any], int]] = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sourceapi.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'app': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
