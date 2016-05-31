__author__ = 'daniel_cruz'

import django_tables2 as tables
from models import Banco, Condominio
from utils import dictfetchall
from django.db import connection
from django_tables2.utils import A
from explorer.models import Query


class RepoTable(tables.Table):
    fecha_Inicial = tables.Column(accessor='fecha_inicio')
    fecha_final = tables.Column(accessor='fecha_fin')
    monto = tables.Column()
    pago = tables.Column()
    dif = tables.Column()
    tipo = tables.Column()

    class Meta:
        orderable = True
#
#
#
class QueriesTable(tables.Table):
    title = tables.Column(verbose_name='Consulta')
    description = tables.Column(verbose_name='Descripcion')

    class Meta:
        model = Query
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ('title', 'description')

class CuentasTable(tables.Table):
    clabe = tables.Column()
    #condominio = tables.LinkColumn('condominos_detail', args=[A('nombre')], accessor='nombre')
    condominio = tables.Column(accessor='nombre')
    apoderado = tables.Column()
    saldo = tables.Column()
    fecha_saldo = tables.Column()
    #todos =  tables.LinkColumn('movtos_detail', args=[A('id')], accessor='link')

    class Meta:
        attrs = {"class": "paleblue"}
        orderable = True

class MovimientosTable(tables.Table):
    cuenta = tables.Column()
    fecha_movimiento = tables.Column(accessor='fecha')
    descripcion = tables.Column()
    retiro = tables.Column()
    deposito = tables.Column()
    saldo = tables.Column()

    class Meta:
        attrs = {"class": "paleblue"}
        orderable = False

class BancoTable(tables.Table):
    class Meta:
        model = Banco
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}


class CondominioTable(tables.Table):
    nombre = tables.Column(verbose_name='Nombre')

    class Meta:
        model = Condominio
        attrs = {"class": "paleblue"}
        fields = ('nombre','colonia','delegacion',)

class DptoPagoTable(tables.Table):
    depto = tables.Column(order_by=('depto'))
    deposito =  tables.Column()

    class Meta:
        attrs = {"class": "paleblue"}

def my_custom_sql(query):
    cursor = connection.cursor()
    print query
    cursor.execute(query)
    rows = dictfetchall(cursor)
    return rows

