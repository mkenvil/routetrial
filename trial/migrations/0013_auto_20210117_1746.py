# Generated by Django 3.1.4 on 2021-01-17 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0012_auto_20210117_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matatuinfo',
            name='Voyage',
        ),
        migrations.AddField(
            model_name='matatuinfo',
            name='voyage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trial.routedestinations'),
        ),
    ]
