# Generated by Django 3.1.4 on 2021-02-10 08:05

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0014_auto_20210209_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depotstage',
            name='depotLocation',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]