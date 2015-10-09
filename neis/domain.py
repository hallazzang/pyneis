# coding: utf-8

DOMAIN_TABLE = (
    ((u'서울특별시',), 'hes.sen.go.kr'),
    ((u'부산광역시',), 'hes.pen.go.kr'),
    ((u'대구광역시',), 'hes.dge.go.kr'),
    ((u'인천광역시',), 'hes.ice.go.kr'),
    ((u'광주광역시',), 'hes.gen.go.kr'),
    ((u'대전광역시',), 'hes.dje.go.kr'),
    ((u'울산광역시',), 'hes.use.go.kr'),
    ((u'세종특별자치시',), 'hes.sje.go.kr'),
    ((u'경기도',), 'hes.goe.go.kr'),
    ((u'강원도',), 'hes.kwe.go.kr'),
    ((u'충청북도', u'충북'), 'hes.cbe.go.kr'),
    ((u'충청남도', u'충남'), 'hes.cne.go.kr'),
    ((u'전라북도', u'전북'), 'hes.jbe.go.kr'),
    ((u'전라남도', u'전남'), 'hes.jne.go.kr'),
    ((u'경상북도', u'경북'), 'hes.gbe.kr'),
    ((u'경상남도', u'경남'), 'hes.gne.go.kr'),
    ((u'제주특별자치도', u'제주도'), 'hes.jje.go.kr'),
)

def get_proper_domain(region_name, encoding='utf-8'):
    if not isinstance(region_name, unicode):
        region_name = region_name.decode(encoding)

    for names, domain in DOMAIN_TABLE:
        for name in names:
            if region_name in name:
                return domain

    return None