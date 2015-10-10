from __future__ import unicode_literals

import requests

from . import USER_AGENT

class RequestClient(object):
    def __init__(self, domain):
        self.domain = domain

    def post(self, path, data, add_headers=None):
        url = 'http://{}{}'.format(self.domain, path)

        headers = {
            'User-Agent': USER_AGENT,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        if add_headers:
            basic_headers.update(add_headers)

        return requests.post(url, data, headers=headers)