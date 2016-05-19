from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import os

@login_required()
def home(request):
     #print os.path.dirname(os.path.dirname(__file__))
     return render_to_response('home/home.html', context_instance=RequestContext(request))


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

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]