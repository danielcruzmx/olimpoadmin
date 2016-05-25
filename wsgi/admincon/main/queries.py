__author__ = 'daniel_cruz'

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