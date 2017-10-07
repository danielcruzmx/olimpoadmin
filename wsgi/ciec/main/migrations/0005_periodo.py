# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160518_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicial', models.DateField(null=True, blank=True)),
                ('fecha_final', models.DateField(null=True, blank=True)),
                ('condominio', models.ForeignKey(to='main.Condominio')),
            ],
            options={
                'db_table': 'periodo',
                'managed': True,
            },
        ),
    ]
