from django.db import models

# CATALOGOS

class Situacion(models.Model):
    situacion = models.CharField(max_length=25)

    def __str__(self):
        return '%s' % (self.situacion)

    class Meta:
        managed = True
        db_table = 'situacion'

class Servicio(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return '%s' % (self.descripcion)

    class Meta:
        managed = True
        db_table = 'servicio'

class TipoMovimiento(models.Model):
    descripcion = models.CharField(max_length=25)

    def __str__(self):
        return '%s' % (self.descripcion)

    class Meta:
        managed = True
        db_table = 'tipo_movimiento'

class TipoCuenta(models.Model):
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.descripcion)

    class Meta:
        managed = True
        db_table = 'tipo_cuenta'

class TipoCuota(models.Model):
    tipo = models.CharField(max_length=20)
    monto_minimo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    monto_maximo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.tipo)

    class Meta:
        managed = True
        db_table = 'tipo_cuota'

class Estacionamiento(models.Model):
    ubicacion = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.ubicacion)

    class Meta:
        managed = True
        db_table = 'estacionamiento'

class Banco(models.Model):
    clave = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.clave, self.descripcion)

    class Meta:
        managed = True
        db_table = 'banco'

# ENTIDADES

class Condominio(models.Model):
    nombre = models.CharField(max_length=45)
    calle = models.CharField(max_length=45, blank=True, null=True)
    colonia = models.CharField(max_length=45, blank=True, null=True)
    delegacion = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    regimen = models.CharField(max_length=45, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    fecha_constitucion = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        managed = True
        db_table = 'condominio'

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
    condominio = models.ForeignKey(Condominio)
    estacionamiento = models.ManyToManyField(Estacionamiento)
    monto_cuota_mes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mes_pagado = models.CharField(max_length=30, blank=True, null=True)
    monto_adeudo_cuotas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_adeudo_extras = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.depto, self.poseedor)

    class Meta:
        managed = True
        db_table = 'condomino'
        ordering = ['depto']

class Cuenta(models.Model):
    cuenta = models.CharField(max_length=20)
    clabe = models.CharField(max_length=18)
    apoderado = models.CharField(max_length=60)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_saldo = models.DateField(blank=True, null=True)
    situacion = models.IntegerField(blank=True, null=True)
    banco = models.ForeignKey(Banco)
    condominio = models.ForeignKey(Condominio)
    tipo_cuenta = models.ForeignKey(TipoCuenta)

    def __str__(self):
        return '%s %s' % (self.clabe, self.apoderado[:10])

    class Meta:
        managed = True
        db_table = 'cuenta'

class Cuota(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    pago = models.DecimalField(max_digits=9, decimal_places=2)
    situacion = models.ForeignKey(Situacion)
    tipo_cuota = models.ForeignKey(TipoCuota)
    condomino = models.ForeignKey(Condomino)

    def __str__(self):
		return '%s' % (self.monto)

    class Meta:
        managed = True
        db_table = 'cuota'

class Recibo(models.Model):
    folio = models.IntegerField(blank=False, null=False)
    fecha = models.DateField()
    notas = models.CharField(max_length=45, blank=True, null=True)
    situacion = models.ForeignKey(Situacion, blank=True, null=True)
    monto = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    cuota = models.ManyToManyField(Cuota)

    class Meta:
        managed = True
        db_table = 'recibo'

class Movimiento(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    fecha = models.DateField(blank=True, null=True)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    retiro = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    deposito = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recibo = models.ManyToManyField(Recibo)

    def __str__(self):
        return u'%d %s %d %s' % (self.id, self.fecha.strftime('%d/%m/%Y'), self.deposito, self.descripcion[:15])

    class Meta:
        managed = True
        db_table = 'movimiento'
        ordering = ['fecha']

class Proveedore(models.Model):
    proveedor =  models.CharField(max_length=60)
    domicilio =  models.CharField(max_length=100, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    servicio = models.ManyToManyField(Servicio)

    def __str__(self):
        return '%s %s' % (self.rfc, self.proveedor)

    class Meta:
        managed = True
        db_table = 'proveedore'

