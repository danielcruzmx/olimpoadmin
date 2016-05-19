from django.contrib import admin
from models import Banco, TipoCuenta, Condominio,  Cuenta, Proveedore, \
                   TipoCuota, TipoMovimiento, Situacion, Servicio

class BancoAdmin(admin.ModelAdmin):
    list_display = ('clave','descripcion')

class TipoCuentaAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class SituacionAdmin(admin.ModelAdmin):
    list_display = ('situacion',)

class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class TipoCuotaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'monto_minimo', 'monto_maximo')

class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class CuentaAdmin(admin.ModelAdmin):
    list_display = ('condominio','banco','clabe','apoderado')

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'rfc', 'domicilio')

admin.site.register(Banco, BancoAdmin)
admin.site.register(TipoCuenta, TipoCuentaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(TipoMovimiento, TipoMovimientoAdmin)
admin.site.register(Situacion, SituacionAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(TipoCuota, TipoCuotaAdmin)
admin.site.register(Proveedore, ProveedoresAdmin)