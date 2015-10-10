__version__ = '0.1.7'
__author__ = 'HallaZzang'
__author_email__ = 'hallazzang@gmail.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2015 by HallaZzang'

USER_AGENT = 'pyneis/{}'.format(__version__)

from .client import Client
from .domain import get_proper_domain

__all__ = [
    'Client',
    'get_proper_domain'
]