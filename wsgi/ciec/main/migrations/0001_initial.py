# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=25, null=True, blank=True)),
            ],
            options={
                'db_table': 'banco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('calle', models.CharField(max_length=45, null=True, blank=True)),
                ('colonia', models.CharField(max_length=45, null=True, blank=True)),
                ('delegacion', models.CharField(max_length=45, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=45, null=True, blank=True)),
                ('estado', models.CharField(max_length=45, null=True, blank=True)),
                ('cp', models.CharField(max_length=5, null=True, blank=True)),
                ('regimen', models.CharField(max_length=45, null=True, blank=True)),
                ('rfc', models.CharField(max_length=13, null=True, blank=True)),
                ('fecha_constitucion', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'condominio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Condomino',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('depto', models.CharField(max_length=15, null=True, blank=True)),
                ('propietario', models.CharField(max_length=60, null=True, blank=True)),
                ('poseedor', models.CharField(max_length=60, null=True, blank=True)),
                ('ubicacion', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.CharField(max_length=25, null=True, blank=True)),
                ('telefono', models.CharField(max_length=30, null=True, blank=True)),
                ('fecha_escrituracion', models.DateField(null=True, blank=True)),
                ('referencia', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('condominio', models.ForeignKey(to='main.Condominio')),
            ],
            options={
                'ordering': ['depto'],
                'db_table': 'condomino',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuenta', models.CharField(max_length=20)),
                ('clabe', models.CharField(max_length=18)),
                ('apoderado', models.CharField(max_length=60)),
                ('saldo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('fecha_saldo', models.DateField(null=True, blank=True)),
                ('situacion', models.IntegerField(null=True, blank=True)),
                ('banco', models.ForeignKey(to='main.Banco')),
                ('condominio', models.ForeignKey(to='main.Condominio')),
            ],
            options={
                'db_table': 'cuenta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('monto', models.DecimalField(max_digits=9, decimal_places=2)),
                ('pago', models.DecimalField(max_digits=9, decimal_places=2)),
                ('condomino', models.ForeignKey(to='main.Condomino')),
            ],
            options={
                'db_table': 'cuota',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ubicacion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estacionamiento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('descripcion', models.CharField(max_length=250, null=True, blank=True)),
                ('retiro', models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)),
                ('deposito', models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)),
                ('saldo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('cuenta', models.ForeignKey(to='main.Cuenta')),
            ],
            options={
                'ordering': ['fecha'],
                'db_table': 'movimiento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folio', models.IntegerField()),
                ('fecha', models.DateField()),
                ('notas', models.CharField(max_length=45, null=True, blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)),
                ('cuota', models.ManyToManyField(to='main.Cuota')),
            ],
            options={
                'db_table': 'recibo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Situacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situacion', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'situacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tipo_cuenta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoCuota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20)),
                ('monto_minimo', models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)),
                ('monto_maximo', models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'tipo_cuota',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='recibo',
            name='situacion',
            field=models.ForeignKey(blank=True, to='main.Situacion', null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='recibo',
            field=models.ManyToManyField(to='main.Recibo'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='situacion',
            field=models.ForeignKey(to='main.Situacion'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='tipo_cuota',
            field=models.ForeignKey(to='main.TipoCuota'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='tipo_cuenta',
            field=models.ForeignKey(to='main.TipoCuenta'),
        ),
        migrations.AddField(
            model_name='condomino',
            name='estacionamiento',
            field=models.ManyToManyField(to='main.Estacionamiento'),
        ),
    ]
