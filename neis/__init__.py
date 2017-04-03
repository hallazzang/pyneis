__version__ = '0.2.0'
__author__ = 'hallazzang'
__author_email__ = 'hallazzang@gmail.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2015-2017 by hallazzang'

USER_AGENT = 'pyneis/{}'.format(__version__)

from .client import NeisClient
from .domain import get_proper_domain

__all__ = [
    'NeisClient',
    'get_proper_domain'
]