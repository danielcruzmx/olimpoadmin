
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from utils import dictfetchall
from tables import BancoTable
from models import Banco
from django_tables2 import RequestConfig
from django.shortcuts import render
from tables import my_custom_sql
from queries import q_movto_mes

@login_required()
def home(request):
    return render_to_response('home/home.html', context_instance=RequestContext(request))

@login_required()
def banco_list(request):
    table = BancoTable(Banco.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'home/lista_bancos.html', {'table': table})

@login_required()
def movtos_list(request):
    datos = my_custom_sql(q_movto_mes('sadicarnot','2016-05-01','2016-05-31'))
    #RequestConfig(request).configure(datos)
    return render_to_response('home/lista_movtos.html', {'table': datos})

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

