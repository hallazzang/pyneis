# coding: utf-8

from __future__ import unicode_literals

import sys

DOMAIN_TABLE = (
    (('서울특별시',), 'hes.sen.go.kr'),
    (('부산광역시',), 'hes.pen.go.kr'),
    (('대구광역시',), 'hes.dge.go.kr'),
    (('인천광역시',), 'hes.ice.go.kr'),
    (('광주광역시',), 'hes.gen.go.kr'),
    (('대전광역시',), 'hes.dje.go.kr'),
    (('울산광역시',), 'hes.use.go.kr'),
    (('세종특별자치시',), 'hes.sje.go.kr'),
    (('경기도',), 'hes.goe.go.kr'),
    (('강원도',), 'hes.kwe.go.kr'),
    (('충청북도', '충북'), 'hes.cbe.go.kr'),
    (('충청남도', '충남'), 'hes.cne.go.kr'),
    (('전라북도', '전북'), 'hes.jbe.go.kr'),
    (('전라남도', '전남'), 'hes.jne.go.kr'),
    (('경상북도', '경북'), 'hes.gbe.kr'),
    (('경상남도', '경남'), 'hes.gne.go.kr'),
    (('제주특별자치도', '제주도'), 'hes.jje.go.kr'),
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