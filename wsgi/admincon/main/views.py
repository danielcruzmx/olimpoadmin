
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework import status
from django.db import connection
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from utils import dictfetchall
from tables import BancoTable, CondominioTable, DptoPagoTable, CuentasTable, QueriesTable
from models import Banco, Condominio
from django_tables2 import RequestConfig
from django.shortcuts import render
from tables import my_custom_sql
from queries import q_movto_mes, q_depto_mes_pago, q_cuentas, q_consultas
from explorer.models import Query
from models import Condominio

#
#   Vistas en operacion
#
@login_required()
def home(request):
    return HttpResponseRedirect('/admin/main')
#    condominios = Condominio.objects.all()
#    return render_to_response('home/home.html', {'condominios':condominios } ,context_instance=RequestContext(request))
#
@login_required()
def query_list(request):
    table = my_custom_sql(q_consultas())
    titulo = 'Datos para descarga'
    keys = ['id','Titulo','Descripcion']
    return render_to_response('admin/descargas.html', { 'table': table, 'titulo': titulo, 'keys': keys} , context_instance=RequestContext(request))
#
#   Vistas de prueba
#
@login_required()
def cuentas_list(request):
    table = CuentasTable(my_custom_sql(q_cuentas()))
    RequestConfig(request).configure(table)
    titulo = 'Cuentas bancarias por condominio'
    return render(request, 'home/lista_comun.html', {'table': table, 'titulo': titulo})

@login_required()
def banco_list(request):
    table = BancoTable(Banco.objects.all())
    RequestConfig(request).configure(table)
    titulo = 'Lista de Bancos'
    return render(request, 'home/lista_comun.html', {'table': table, 'titulo': titulo})

@login_required()
def querys_list(request):
    table = QueriesTable(Query.objects.all())
    RequestConfig(request).configure(table)
    titulo = 'Lista de datos a descargar'
    return render(request, 'home/lista_comun.html', {'table': table, 'titulo': titulo})

@login_required()
def condominio_list(request):
    table = CondominioTable(Condominio.objects.all())
    #print table
    RequestConfig(request).configure(table)
    return render(request, 'home/lista_condominios.html', {'table': table})

@login_required()
def movtos_list(request):
    table = my_custom_sql(q_movto_mes('sadicarnot','2016-05-01','2016-05-31'))
    RequestConfig(request).configure(table)
    return render(request, 'home/lista_condominios.html', {'table': table})

def pago_depto_list(request):
    table = DptoPagoTable(my_custom_sql(q_depto_mes_pago('sadicarnot','2016-05-01','2016-05-31')))
    #print table
    RequestConfig(request).configure(table)
    return render(request, 'home/lista_condominios.html', {'table': table})

class CondominoViewSet(APIView):

    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        #get_arg1 = request.GET.get('mail_id')
        valor = kw['mail_id']
        query = '''
    		 Select co.nombre, cn.depto, cn.fecha_ultimo_deposito, cn.monto_cuota_mes, cn.referencia,
                   ba.descripcion, cu.apoderado, cu.cuenta, cu.clabe
            From condomino cn, condominio co, cuenta cu, banco ba
            where cn.condominio_id = co.id
            and   co.id = cu.condominio_id
            and   cu.banco_id = ba.id
            and   cn.email = '%s'
		''' % valor
        #for k,v in request.GET.get.items():
        #    print k,v
        #print kw['mail_id']
        print query
        cursor.execute(query)
        cuotas_list = dictfetchall(cursor)
        response = Response(cuotas_list, status=status.HTTP_200_OK)
        return response

