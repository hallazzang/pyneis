# coding: utf-8

from __future__ import unicode_literals

import sys

ALLERGY_TABLE = (
    ('①', '난류'),
    ('②', '우유'),
    ('③', '메밀'),
    ('④', '땅콩'),
    ('⑤', '대두'),
    ('⑥', '밀'),
    ('⑦', '고등어'),
    ('⑧', '게'),
    ('⑨', '새우'),
    ('⑩', '돼지고기'),
    ('⑪', '복숭아'),
    ('⑫', '토마토'),
    ('⑬', '아황산염')
)

class Menu(object):
    @property
    def text(self):
        return self._text

    @property
    def allergy(self):
        return self._allergy

    def __repr__(self):
        ret = '<Menu: {}>'.format(self.text)

        if sys.version_info.major == 2:
            return ret.encode(sys.stdout.encoding or 'utf-8')
        else:
            return ret

class Meal(object):
    @property
    def date(self):
        return self._date

    @property
    def type(self):
        return self._type

    @property
    def menus(self):
        return self._menus

    def __repr__(self):
        if len(self.menus) == 0:
            return '<Meal: Empty>'
        else:
            return '<Meal: {} Menus>'.format(len(self.menus))