# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condomino',
            name='fecha_ultimo_deposito',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='condomino',
            name='monto_cuota_mes',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
