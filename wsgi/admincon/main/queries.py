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


