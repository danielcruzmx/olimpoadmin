# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160516_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'tipo_movimiento',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='movimiento',
            name='tipo_movimiento',
            field=models.ForeignKey(blank=True, to='main.TipoMovimiento', null=True),
        ),
    ]
