# coding: utf-8

from __future__ import unicode_literals

import sys
import re
from datetime import date

import requests

from .meal import Menu, Meal

class School(object):
    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @property
    def course(self):
        return self._course

    def __repr__(self):
        ret = '<School: {}>'.format(self.name)

        if sys.version_info.major == 2:
            return ret.encode(sys.stdout.encoding or 'utf-8')
        else:
            return ret

    def get_weekly_meals(self, year, month, day, type):
        """
        type: 1(breakfast), 2(lunch), 3(dinner)
        """

        data = {
            'insttNm': self._name,
            'schMmealScCode': type,
            'schYmd': '%d%02d%02d' % (year, month, day),
            'schulCode': self.code,
            'schulCrseScCode': self.course,
            'schulKndScCode': '%02d' % (self.course)
        }

        r = self._client._request('post', '/sts_sci_md01_001.ws', json=data).json()

        meals = []

        for day in ('sun', 'mon', 'tue', 'wed', 'the', 'fri', 'sat'):
            menus = []

            for chunk in r['resultSVO']['weekDietList'][2][day].split('<br />')[:-1]:
                searched = re.search(r'(?:\d{1,2}\.)+', chunk)
                allergy = searched.group(0) if searched else None

                menu = Menu()
                menu._text = re.sub(r'(?:\d{1,2}\.)*', '', chunk)
                menu._allergy = allergy

                menus.append(menu)

            y, m, d = map(
                int,
                re.search(r'^(\d{4})\.(\d{2})\.(\d{2})',
                          r['resultSVO']['weekDietList'][0][day]).groups()
            )

            meal = Meal()
            meal._date = date(y, m, d)
            meal._type = type
            meal._menus = menus

            meals.append(meal)

        return meals