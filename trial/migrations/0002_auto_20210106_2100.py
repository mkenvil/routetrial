# Generated by Django 3.1.4 on 2021-01-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='depotstage',
            options={'verbose_name_plural': 'Depotstage'},
        ),
        migrations.AlterModelOptions(
            name='matatuinfo',
            options={'verbose_name_plural': 'MatatuInfo'},
        ),
        migrations.AlterModelOptions(
            name='passengerinfo',
            options={'verbose_name_plural': 'Passengerinfo'},
        ),
        migrations.AddField(
            model_name='depotstage',
            name='depotname',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
