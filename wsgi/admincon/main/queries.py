__author__ = 'daniel_cruz'
#
#    Consultas empleadas
#
def q_hist_cuotas(tabla, condomino):
    query = '''
                select ELT(DATE_FORMAT(fecha_inicio,'%m'),'Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic')  as ini,
                       ELT(DATE_FORMAT(fecha_fin,'%m'),'Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic')  as fin,
                       monto, pago, monto-pago as adeudo, tipo_cuota.tipo as tipo,
                       depto, propietario
                from  %s_cuota, tipo_cuota, situacion, %s_condomino
                where %s_cuota.tipo_cuota_id = tipo_cuota.id
                and   %s_cuota.situacion_id = situacion.id
                and   %s_cuota.condomino_id = %s_condomino.id
                and   condomino_id = %s
                and   fecha_fin <= now()
                order by fecha_inicio
    ''' % (tabla,tabla,tabla,tabla,tabla,tabla,condomino)
    return query
#
#
#
def q_adeudos_condomino(tabla, condomino):
    query = '''
        select
        year(fecha_fin) as anio, tipo_cuota.tipo, sum(monto) as monto, sum(pago) as pago, sum(monto - pago) as adeudo, "detalle" as detalle,
        depto, propietario
        from  %s_cuota, tipo_cuota, situacion, %s_condomino
        where %s_cuota.tipo_cuota_id = tipo_cuota.id
        and   %s_cuota.situacion_id = situacion.id
        and   %s_cuota.condomino_id = %s_condomino.id
        and   condomino_id = %s
        and   fecha_fin <= now()
        group by anio, tipo, depto, propietario
        order by 1
    ''' % (tabla,tabla,tabla,tabla,tabla,tabla,condomino)
    return query
#
#
#
def q_movto_mes(tabla, fecha_ini, fecha_fin):
    query = '''
        select m.id,
               fecha as fec_ini,
               fecha as fec_fin,
               t.descripcion + ' ' + m.descripcion as descripcion,
               retiro, deposito, saldo, c.depto
        from   %s_movimiento m, tipo_movimiento t, %s_condomino c
        where m.tipo_movimiento_id = t.id
        and   m.condomino_id = c.id
        and fecha >= '%s'
        and fecha <= '%s'
        ORDER BY 2,1
    ''' % (tabla, tabla, fecha_ini, fecha_fin)
    return query

def q_depto_mes_pago(tabla, fecha_ini, fecha_fin):
    query = '''
        select c.depto as depto, deposito
        from   %s_movimiento m, tipo_movimiento t, %s_condomino c
        where m.tipo_movimiento_id = t.id
        and   m.condomino_id = c.id
        and fecha >= '%s'
        and fecha <= '%s'
        ORDER BY 2,1
    ''' % (tabla, tabla, fecha_ini, fecha_fin)
    return query

def q_cuentas():
    query = '''
        SELECT cuenta.id, clabe, trim(nombre) as nombre, apoderado, saldo as saldo, fecha_saldo,
        'Todos' as link
        FROM cuenta, condominio
        where cuenta.condominio_id = condominio.id
        order by fecha_saldo desc
    '''
    return query

def q_consultas():
    query = '''
        SELECT id, title as titulo, description as descripcion
        FROM explorer_query
        order by id
    '''
    return query