from django.db import models

# CATALOGOS COMUNES

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

class Banco(models.Model):
    clave = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.clave, self.descripcion)

    class Meta:
        managed = True
        db_table = 'banco'

# ENTIDADES COMUNES

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
        return '%s %s %s' % (self.condominio, self.clabe, self.apoderado[:10])

    class Meta:
        managed = True
        db_table = 'cuenta'

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


