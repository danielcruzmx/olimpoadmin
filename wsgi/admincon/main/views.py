
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
from datetime import datetime
from queries import q_hist_cuotas, q_adeudos_condomino
#
#   Vistas en operacion
#
@login_required()
def home(request):
    return HttpResponseRedirect('/admin/main')
#
@login_required()
def reporte_cuotas(request,condominio,idCondomino):
    idCondomino = int(idCondomino)
    table = my_custom_sql(q_hist_cuotas(condominio,idCondomino))
    titulo = 'Condominio ' + str(condominio).upper() + ', historico de cuotas del condomino '
    keys = ['inicio','fin','monto','pago','adeudo','tipo']
    return render_to_response(
        "home/reportcuotas.html",
        {'table'        : table,
         'titulo'       : titulo,
         'keys'         : keys,
         'current_date' : datetime.now() },
         context_instance=RequestContext(request, {}),
    )
#
@login_required()
def reporte_adeudos(request,condominio,idCondomino):
    idCondomino = int(idCondomino)
    table = my_custom_sql(q_adeudos_condomino(condominio,idCondomino))
    titulo = 'Condominio ' + str(condominio).upper() + ', historico de cuotas del condomino '
    keys = ['anio','tipo','monto','pago','adeudo','detalle']
    return render_to_response(
        "home/reportadeudos.html",
        {'table'        : table,
         'titulo'       : titulo,
         'keys'         : keys,
         'current_date' : datetime.now() },
         context_instance=RequestContext(request, {}),
    )
#
#   Vistas de prueba
#
@login_required()
def query_list(request):
    table = my_custom_sql(q_consultas())
    titulo = 'Datos para descarga'
    keys = ['id','Titulo','Descripcion']
    return render_to_response('admin/descargas.html', { 'table': table, 'titulo': titulo, 'keys': keys} , context_instance=RequestContext(request))

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
            From olimpo_condomino cn, condominio co, cuenta cu, banco ba
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

class CuotasViewSet(APIView):

    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        #get_arg1 = request.GET.get('mail_id')
        valor = kw['depto_id']
        query = '''
                SELECT olimpo_movimiento.id as Num,fecha AS fecha,tipo_movimiento.descripcion AS tipo,
                       olimpo_movimiento.descripcion AS descripcion, CONCAT(olimpo_condomino.depto,' ',olimpo_condomino.propietario) as Condomino,
                       retiro as cargo, deposito as abono,  saldo
                FROM olimpo_movimiento,
                    tipo_movimiento,
                     olimpo_condomino,
                     periodo,
                     condominio
                WHERE olimpo_movimiento.tipo_movimiento_id = tipo_movimiento.id
                AND olimpo_movimiento.condomino_id = olimpo_condomino.id
                and periodo.condominio_id = condominio.id
                and olimpo_condomino.condominio_id = condominio.id
                and olimpo_condomino.depto = '%s'
                ORDER BY 2,1

        ''' % valor
        #for k,v in request.GET.get.items():
        #    print k,v
        #print kw['mail_id']
        #print query
        #cursor.execute(query)
        cursor.callproc("saldo_movimientos_depto", [valor])
        cuotas_list = dictfetchall(cursor)
        response = Response(cuotas_list, status=status.HTTP_200_OK)
        return response

class CondominosOlimpoViewSet(APIView):

    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        query = '''
             Select co.nombre as CONDOMINIO, cn.depto AS DEPTO, cn.propietario as CONDOMINO
             From olimpo_condomino cn, condominio co
             where cn.condominio_id = co.id
    		''' 
        print query
        cursor.execute(query)
        condominos_list = dictfetchall(cursor)
        response = Response(condominos_list, status=status.HTTP_200_OK)
        return response


class FaltantesMesOlimpoViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valor = kw['mes_anio']
        query = '''
                SELECT nombre as CONDOMINIO,
                       '%s' as MES, 
                       depto as DEPTO,
                       propietario as CONDOMINO, 
                       email as CORREO,
                       telefono as TELEFONO
                FROM olimpo_condomino,
                     condominio
                WHERE olimpo_condomino.condominio_id = condominio.id
	            and depto NOT IN
                        (SELECT depto
                         FROM olimpo_movimiento,
                              cuenta,
                              olimpo_condomino
                         WHERE olimpo_movimiento.cuenta_id = cuenta.id
                         AND date_format(fecha,'%%m-%%Y') = '%s'      
                         AND olimpo_condomino.id = olimpo_movimiento.condomino_id
                         AND olimpo_condomino.depto != '0000'
                         AND deposito > 0)
                and depto != '0000'       
                ORDER BY depto
                ''' % (valor,valor)
        cursor.execute(query)
        faltantes_list = dictfetchall(cursor)
        response = Response(faltantes_list, status=status.HTTP_200_OK)
        return response

class CuotasDeptoMesOlimpoViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valor = kw['mes_anio']
        #print valor
        query = '''
                SELECT '%s' as MES,
                       nombre as CONDOMINIO,
                       depto as DEPTO,
                       propietario as PROPIETARIO,
                       sum(deposito) as DEPOSITO
                FROM olimpo_movimiento, cuenta, olimpo_condomino, condominio
                WHERE olimpo_movimiento.cuenta_id = cuenta.id
                      and date_format(fecha,'%%m-%%Y') = '%s'
                      and olimpo_condomino.id = olimpo_movimiento.condomino_id
                      and cuenta.condominio_id = condominio.id
                      and olimpo_condomino.depto != '0000'
                      and deposito > 0
                GROUP by 1,2,3,4
                UNION
                SELECT '%s' as MES,
                       nombre as CONDOMINIO,
                       depto as DEPTO,
                       propietario AS PROPIETARIO,
                       0 AS DEPOSITO
                FROM olimpo_condomino, condominio
                WHERE olimpo_condomino.condominio_id = condominio.id
                      and depto NOT IN
                         (SELECT depto
                          FROM olimpo_movimiento,
                               cuenta,
                               olimpo_condomino
                          WHERE olimpo_movimiento.cuenta_id = cuenta.id
                          AND olimpo_condomino.id = olimpo_movimiento.condomino_id
                          and cuenta.condominio_id = condominio.id
                          AND olimpo_condomino.depto != '0000'
                          AND date_format(fecha,'%%m-%%Y') = '%s'
                          AND deposito > 0)
                 AND depto != '0000'       
                 ORDER BY depto
        ''' % (valor, valor, valor, valor)
        #print query
        cursor.execute(query)
        cuotas_list = dictfetchall(cursor)
        response = Response(cuotas_list, status=status.HTTP_200_OK)
        return response

class MovimientosOlimpoViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorIni = kw['fec_ini']
        valorFin = kw['fec_fin']
        #print valor
        query = '''
             SELECT olimpo_movimiento.id as NUM,
                   fecha AS FECHA,
                   tipo_movimiento.descripcion AS TIPO,
                   olimpo_movimiento.descripcion AS DESCRIPCION,
                   CONCAT(olimpo_condomino.depto,' ', olimpo_condomino.propietario) AS CONDOMINO,
                   retiro AS RETIRO,
                   deposito AS DEPOSITO,
                   saldo AS SALDO,
                   olimpo_condomino.depto AS DEPTO
            FROM olimpo_movimiento,
                 tipo_movimiento,
                 olimpo_condomino,
                 condominio
            WHERE olimpo_movimiento.tipo_movimiento_id = tipo_movimiento.id
                  AND olimpo_movimiento.condomino_id = olimpo_condomino.id
                  AND olimpo_condomino.condominio_id = condominio.id
                  AND fecha >= '%s'
                  AND fecha <= '%s'
            ORDER BY 2,1
        ''' % (valorIni, valorFin)
        #print query
        cursor.execute(query)
        movimientos_list = dictfetchall(cursor)
        response = Response(movimientos_list, status=status.HTTP_200_OK)
        return response

class NoIdentificadosOlimpoViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorIni = kw['fec_ini']
        valorFin = kw['fec_fin']
        #print valor
        query = '''
           SELECT nombre as CONDOMINIO,
                  cuenta as CUENTA,
                  fecha AS FECHA,
                  descripcion AS DESCRIPCION,
                  deposito AS DEPOSITO
           FROM olimpo_movimiento,
                cuenta,
                olimpo_condomino,
                condominio
           WHERE olimpo_movimiento.cuenta_id = cuenta.id
           AND FECHA >= '%s'
           AND FECHA <= '%s'
           AND olimpo_condomino.id = olimpo_movimiento.condomino_id
           AND olimpo_condomino.depto = '0000'
           AND cuenta.condominio_id = condominio.id
           AND deposito > 0
           ORDER BY FECHA
        ''' % (valorIni, valorFin)
        #print query
        cursor.execute(query)
        movimientos_list = dictfetchall(cursor)
        response = Response(movimientos_list, status=status.HTTP_200_OK)
        return response

class TotalIngresosEgresosOlimpoViewSet(APIView):
    def get(self, request, *args, **kw):
        cursor = connection.cursor()
        valorIni = kw['fec_ini']
        valorFin = kw['fec_fin']
        #print valor
        query = '''
           SELECT nombre AS CONDOMINIO,
                  cuenta as CUENTA,
                  cuenta.saldo as SALDO,
                  MIN(olimpo_movimiento.FECHA) AS FECHAINI,
                  MAX(olimpo_movimiento.FECHA) AS FECHAFIN,
                  SUM(olimpo_movimiento.RETIRO) AS RETIROS,
                  SUM(olimpo_movimiento.deposito) AS DEPOSITOS,
                  sum(deposito) - sum(retiro) AS SALDO
           FROM olimpo_movimiento,
                cuenta,
                condominio
           WHERE cuenta.id = olimpo_movimiento.cuenta_id
           AND FECHA >= '%s'
           AND FECHA <= '%s'
           AND cuenta.condominio_id = condominio.id
           GROUP BY cuenta
        ''' % (valorIni, valorFin)
        #print query
        cursor.execute(query)
        totales_list = dictfetchall(cursor)
        response = Response(totales_list, status=status.HTTP_200_OK)
        return response