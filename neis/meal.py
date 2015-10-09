# coding: utf-8

import sys

ALLERGY_TABLE = (
    (u'①', u'난류'),
    (u'②', u'우유'),
    (u'③', u'메밀'),
    (u'④', u'땅콩'),
    (u'⑤', u'대두'),
    (u'⑥', u'밀'),
    (u'⑦', u'고등어'),
    (u'⑧', u'게'),
    (u'⑨', u'새우'),
    (u'⑩', u'돼지고기'),
    (u'⑪', u'복숭아'),
    (u'⑫', u'토마토'),
    (u'⑬', u'아황산염')
)

class Menu(object):
    @property
    def text(self):
        return self._text

    @property
    def allergy(self):
        return self._allergy

    def __repr__(self):
        text = self.text.encode(sys.stdout.encoding or 'utf-8')
        return '<Menu: {}>'.format(text)

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