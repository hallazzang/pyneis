from __future__ import unicode_literals

import sys

from .school import School
from .domain import get_proper_domain
from .request import RequestClient

class Client(object):
    def __init__(self, region_name, **kwargs):
        self.domain = get_proper_domain(region_name)
        if not self.domain:
            raise ValueError('unable to find proper domain '
                             'for given region name')

        self._request_client = RequestClient(self.domain)

    def __repr__(self):
        return '<NeisClient: {}>'.format(self.domain)

    def search_school(self, school_name):
        if sys.version_info.major == 2:
            if isinstance(school_name, str):
                school_name = school_name.decode(sys.stdout.encoding or 'utf-8')

        data = {
            'kraOrgNm': school_name,
            'atptOfcdcScCode': '',
            'srCode': ''
        }

        response = self._request_client.post('/spr_ccm_cm01_100.do', data)
        response = response.json()

        result = []
        for item in response['resultSVO']['data']['orgDVOList']:
            school = School()

            school._request_client = RequestClient(self.domain)
            school._name = item['kraOrgNm']
            school._code = item['orgCode']
            school._course = int(item['schulCrseScCode'])

            result.append(school)

        return result