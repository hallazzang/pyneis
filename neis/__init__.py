from __future__ import unicode_literals

__version__ = '0.1.1'
__author__ = 'Halla Kim'
__license__ = 'MIT'
__email__ = 'hallazzang@gmail.com'

USER_AGENT = 'pyneis/{}'.format(__version__)

from .client import Client
from .domain import get_proper_domain

__all__ = [
    'Client',
    'get_proper_domain'
]