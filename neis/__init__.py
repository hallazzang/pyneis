__version__ = '0.1'
__author__ = 'HallaZzang'
__license__ = 'MIT Licence'
__email__ = 'hallazzang@gmail.com'

USER_AGENT = 'pyneis/{}'.format(__version__)

from neis.client import Client
from neis.domain import get_proper_domain

__all__ = [
    'Client',
    'get_proper_domain'
]