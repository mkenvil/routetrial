import os
from django.contrib.gis.utils import LayerMapping
from .models import Mainroads

mainroads_mapping = {
    'kenroad_id': 'KENROAD_ID',
    'geom': 'MULTILINESTRING',
}


mainroads_shp = os.path .abspath(
    os.path.join(os.path.dirname(__file__), 'ke-major-roads/ke_major-roads.shp')
)

def run(verbose=True):
    lm = LayerMapping(Mainroads, mainroads_shp, mainroads_mapping, transform=False, encoding='iso-8859-1')
    lm.save(verbose=verbose, strict=True)
