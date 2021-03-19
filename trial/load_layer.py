import os
from django.contrib.gis.utils import LayerMapping
from .models import Roads

roads_mapping = {
    'id': 'id',
    'osm_id': 'osm_id',
    'sourceid': 'sourceid',
    'notes': 'notes',
    'onme': 'onme',
    'rtenme': 'rtenme',
    'ntlclass': 'ntlclass',
    'fclass': 'fclass',
    'numlanes': 'numlanes',
    'srftpe': 'srftpe',
    'srfcond': 'srfcond',
    'isseasonal': 'isseasonal',
    'curntprac': 'curntprac',
    'gnralspeed': 'gnralspeed',
    'rdwidthm': 'rdwidthm',
    'status': 'status',
    'iselevated': 'iselevated',
    'iso3': 'iso3',
    'country': 'country',
    'last_updat': 'last_updat',
    'geom': 'MULTILINESTRING',
}


roads_shp = os.path .abspath(
    os.path.join(os.path.dirname(__file__), 'ke-trs-roads/ken_trs_roads_osm.shp')
)


def run(verbose=True):
    lm = LayerMapping(Roads, roads_shp, roads_mapping, transform=False, encoding='iso-8859-1')
    lm.save(verbose=verbose, strict=True)
