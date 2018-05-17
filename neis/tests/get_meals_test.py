# coding: utf-8

from neis import NeisClient


def test_get_weekly_meals():
    client = NeisClient(u'서울')
    school = client.search_school(u'휘문고등학교')[0]
    meals = school.get_weekly_meals(2015, 10, 10, 2)
    assert len(meals) == 7
    assert not meals[0].menus
    assert len(meals[1].menus) == 6
    assert meals[1].menus[2].text == u'안동찜닭'
