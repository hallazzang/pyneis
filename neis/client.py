from __future__ import unicode_literals

import sys

import requests

from .school import School
from .domain import get_proper_domain

class NeisClient(object):
    def __init__(self, region_name, **kwargs):
        self.domain = get_proper_domain(region_name)
        if not self.domain:
            raise ValueError('unable to find proper domain '
                             'for given region name')

        self._session = requests.Session()
        self._session_freshed = False

    def __repr__(self):
        return '<NeisClient: {}>'.format(self.domain)

    def search_school(self, school_name):
        if sys.version_info.major == 2:
            if isinstance(school_name, str):
                school_name = school_name.decode(sys.stdout.encoding or 'utf-8')

        data = {
            'kraOrgNm': school_name,
        }

        r = self._request('post', '/spr_ccm_cm01_100.ws', json=data).json()

        result = []
        for item in r['resultSVO']['orgDVOList']:
            school = School()

            school._client = self
            school._name = item['kraOrgNm']
            school._code = item['orgCode']
            school._course = int(item['schulCrseScCode'])

            result.append(school)

        return result

    def _request(self, method, path, **kwargs):
        if not self._session_freshed:
            self._session_freshed = True
            self._request('get', '/edusys.jsp?page=sts_m40000&returnDomain=S10')

        url = 'http://%s%s' % (self.domain, path)

        return self._session.request(method=method, url=url, **kwargs)