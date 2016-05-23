__author__ = 'daniel_cruz'

import django_tables2 as tables
from models import Banco
from utils import dictfetchall
from django.db import connection

class BancoTable(tables.Table):
    class Meta:
        model = Banco
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

def my_custom_sql(query):
    cursor = connection.cursor()
    print query
    cursor.execute(query)
    rows = dictfetchall(cursor)
    return rows

