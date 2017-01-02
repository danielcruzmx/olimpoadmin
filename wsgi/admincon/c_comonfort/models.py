from django.db import models

from main.models import Situacion, TipoMovimiento,  \
                        TipoCuota, Condominio, Cuenta

class Estacionamiento(models.Model):
    ubicacion = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return u'%s' % (self.ubicacion)

    class Meta:
        managed = True
        db_table = 'comonfort_estacionamiento'

class Condomino(models.Model):
    depto = models.CharField(max_length=15, blank=True, null=True)
    propietario = models.CharField(max_length=60, blank=True, null=True)
    poseedor = models.CharField(max_length=60, blank=True, null=True)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    fecha_escrituracion = models.DateField(blank=True, null=True)
    fecha_ultimo_deposito = models.DateField(blank=True, null=True)
    referencia = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    condominio = models.ForeignKey(Condominio, related_name='comonfort_condomino_condominio_id')
    estacionamiento = models.ManyToManyField(Estacionamiento, related_name='comonfort_condomino_estacionamiento_id')
    monto_cuota_mes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mes_pagado = models.CharField(max_length=30, blank=True, null=True)
    monto_adeudo_cuotas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_adeudo_extras = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.depto, self.poseedor)

    def cuotas(self):
        return '<a href="/admin/report/cuotas/comonfort/%s/">Detalle</a>' % (self.id)

    cuotas.allow_tags = True

    class Meta:
        managed = True
        db_table = 'comonfort_condomino'
        ordering = ['depto']

class Movimiento(models.Model):
    cuenta = models.ForeignKey(Cuenta, related_name='comonfort_movimiento_cuenta_id')
    fecha = models.DateField(blank=True, null=True)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, blank=True, null=True, related_name='comonfort_movimiento_tipo_movimiento_id')
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    condomino = models.ForeignKey(Condomino, related_name='comonfort_movimiento_condomino_id')
    retiro = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    deposito = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    recibo = models.IntegerField(blank=False, null=True, default=0)

    def __str__(self):
        return u'%d %s %d %s' % (self.id, self.fecha.strftime('%d/%m/%Y'), self.deposito, self.descripcion[:15])

    class Meta:
        managed = True
        db_table = 'comonfort_movimiento'
        ordering = ['fecha']

class Auxiliar(models.Model):
    cuenta = models.ForeignKey(Cuenta, related_name='comonfort_auxiliar_cuenta_id')
    fecha = models.DateField(blank=True, null=True)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, blank=True, null=True, related_name='comonfort_auxiliar_tipo_movimiento_id')
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    condomino = models.ForeignKey(Condomino, related_name='comonfort_auxuliar_condomino_id')
    retiro = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    deposito = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    recibo = models.IntegerField(blank=False, null=True, default=0)

    def __str__(self):
        return u'%d %s %d %s' % (self.id, self.fecha.strftime('%d/%m/%Y'), self.deposito, self.descripcion[:15])

    class Meta:
        managed = True
        db_table = 'comonfort_auxiliar'
        ordering = ['fecha']

class Cuota(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    pago = models.DecimalField(max_digits=9, decimal_places=2)
    situacion = models.ForeignKey(Situacion, related_name='comonfort_cuota_situacion_id')
    tipo_cuota = models.ForeignKey(TipoCuota, related_name='comonfort_cuota_tipo_cuota_id')
    condomino = models.ForeignKey(Condomino, related_name='comonfort_cuota_condomino_id')
    movimiento = models.ForeignKey(Movimiento, related_name='comonfort_cuota_movimiento_id')

    def __str__(self):
        return '%s' % (self.monto)

    class Meta:
        managed = True
        db_table = 'comonfort_cuota'

class Recibo(models.Model):
    folio = models.IntegerField(blank=False, null=False)
    fecha = models.DateField()
    condomino = models.ForeignKey(Condomino, related_name='comonfort_recibo_condomino_id')
    monto = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    notas = models.CharField(max_length=45, blank=True, null=True)
    situacion = models.ForeignKey(Situacion, blank=True, null=True, related_name='comonfort_recibo_situacion_id')
    cuota = models.ManyToManyField(Cuota, related_name='comonfort_recibo_cuota_id')

    def __str__(self):
        return '%s' % (self.folio)

    class Meta:
        managed = True
        db_table = 'comonfort_recibo'
