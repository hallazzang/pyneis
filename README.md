# pyneis
python http client for Neis service(http://neis.go.kr/)

[![Build Status](https://travis-ci.org/hallazzang/pyneis.svg?branch=master)](https://travis-ci.org/hallazzang/pyneis)

Installation
------------
```bash
$ pip install pyneis
```

Example
-------
```python
>>> import neis
>>> client = neis.NeisClient('서울')
>>> schools = client.search_school('휘문')
>>> print(schools)
[<School: 휘문중학교>, <School: 휘문고등학교>]

>>> meals = schools[1].get_weekly_meals(2015, 10, 10, 2)
>>> print(meals)
[<Meal: Empty>, <Meal: 6 Menus>, <Meal: 6 Menus>,
 <Meal: 6 Menus>, <Meal: 6 Menus>, <Meal: Empty>, <Meal: Empty>]

>>> print(meals[1].menus)
['혼합잡곡밥', '돈육김치찌개', '안동찜닭',
 '콩나물무침', '삼치살양념구이', '석박지']
```

`School.get_weekly_meals()` takes `year`, `month`, `day` and `type` for parameters.
`type` can be 1(breakfast), 2(lunch), 3(dinner).

Note
----
pyneis is developed in Python 2.7.13
