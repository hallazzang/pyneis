# coding: utf-8

from neis import NeisClient

def test_search_str():
    client = NeisClient('서울')
    assert len(client.search_school('휘문')) == 2
    assert len(client.search_school('휘문고등학교')) == 1

def test_search_unicode():
    client = NeisClient(u'서울')
    assert len(client.search_school(u'휘문')) == 2
    assert len(client.search_school(u'휘문고등학교')) == 1
