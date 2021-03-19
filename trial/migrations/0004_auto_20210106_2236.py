# Generated by Django 3.1.4 on 2021-01-06 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0003_auto_20210106_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteDestinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaceName', models.CharField(max_length=150, null=True)),
                ('Price', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'RouteDestinations',
                'ordering': ['PlaceName'],
            },
        ),
        migrations.AddField(
            model_name='depotstage',
            name='depotdestinations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trial.routedestinations'),
        ),
    ]
