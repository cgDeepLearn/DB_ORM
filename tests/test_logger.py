# -*- coding: utf8 -*-
"""
test logger
"""

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logger import crawler, parser

crawler.info('crawler')
parser.info('parser got something')