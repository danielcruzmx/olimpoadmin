# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160516_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.CharField(max_length=60)),
                ('domicilio', models.CharField(max_length=100, null=True, blank=True)),
                ('rfc', models.CharField(max_length=13, null=True, blank=True)),
            ],
            options={
                'db_table': 'proveedore',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'servicio',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='condomino',
            name='condominio',
        ),
        migrations.RemoveField(
            model_name='condomino',
            name='estacionamiento',
        ),
        migrations.RemoveField(
            model_name='cuota',
            name='condomino',
        ),
        migrations.RemoveField(
            model_name='cuota',
            name='situacion',
        ),
        migrations.RemoveField(
            model_name='cuota',
            name='tipo_cuota',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='cuenta',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='recibo',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='tipo_movimiento',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='cuota',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='situacion',
        ),
        migrations.DeleteModel(
            name='Condomino',
        ),
        migrations.DeleteModel(
            name='Cuota',
        ),
        migrations.DeleteModel(
            name='Estacionamiento',
        ),
        migrations.DeleteModel(
            name='Movimiento',
        ),
        migrations.DeleteModel(
            name='Recibo',
        ),
        migrations.AddField(
            model_name='proveedore',
            name='servicio',
            field=models.ManyToManyField(to='main.Servicio'),
        ),
    ]
