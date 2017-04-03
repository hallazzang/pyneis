# coding: utf-8

from __future__ import unicode_literals

import sys

DOMAIN_TABLE = (
    (('서울특별시', '서울시'), 'stu.sen.go.kr'),
    (('부산광역시', '부산시'), 'stu.pen.go.kr'),
    (('대구광역시', '대구시'), 'stu.dge.go.kr'),
    (('인천광역시', '인천시'), 'stu.ice.go.kr'),
    (('광주광역시', '광주시'), 'stu.gen.go.kr'),
    (('대전광역시', '대전시'), 'stu.dje.go.kr'),
    (('울산광역시', '울산시'), 'stu.use.go.kr'),
    (('세종특별자치시', '세종시'), 'stu.sje.go.kr'),
    (('경기도',), 'stu.goe.go.kr'),
    (('강원도',), 'stu.kwe.go.kr'),
    (('충청북도', '충북'), 'stu.cbe.go.kr'),
    (('충청남도', '충남'), 'stu.cne.go.kr'),
    (('전라북도', '전북'), 'stu.jbe.go.kr'),
    (('전라남도', '전남'), 'stu.jne.go.kr'),
    (('경상북도', '경북'), 'stu.gbe.kr'),
    (('경상남도', '경남'), 'stu.gne.go.kr'),
    (('제주특별자치도', '제주도'), 'stu.jje.go.kr'),
)

def get_proper_domain(region_name):
    if sys.version_info.major == 2:
        if isinstance(region_name, str):
            region_name = region_name.decode(sys.stdout.encoding or 'utf-8')

    for names, domain in DOMAIN_TABLE:
        for name in names:
            if region_name in name:
                return domain

    return None