__author__ = 'daniel_cruz'

import django_tables2 as tables
from models import Banco

class BancoTable(tables.Table):
    class Meta:
        model = Banco
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}