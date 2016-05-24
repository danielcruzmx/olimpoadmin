__author__ = 'daniel_cruz'

import django_tables2 as tables
from models import Banco, Condominio
from utils import dictfetchall
from django.db import connection

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

