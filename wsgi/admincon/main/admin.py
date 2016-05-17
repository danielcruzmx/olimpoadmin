from django.contrib import admin

from django.contrib import admin
from models import Banco, TipoCuenta, Movimiento, Condominio, Condomino, Cuenta, \
                   Estacionamiento, TipoMovimiento, Situacion

class BancoAdmin(admin.ModelAdmin):
	list_display = ('clave','descripcion')

class TipoCuentaAdmin(admin.ModelAdmin):
	list_display = ('descripcion',)

class SituacionAdmin(admin.ModelAdmin):
	list_display = ('situacion',)

class TipoMovimientoAdmin(admin.ModelAdmin):
	list_display = ('descripcion',)

class MovimientoAdmin(admin.ModelAdmin):
	list_display = ('id','fecha','descripcion','retiro','deposito')
	search_fields = ('descripcion',)
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class CondominioAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class CuentaAdmin(admin.ModelAdmin):
	list_display = ('condominio','banco','clabe','apoderado')

class CondominoAdmin(admin.ModelAdmin):
	list_display = ('depto','ubicacion','propietario','poseedor')
	search_fields = ('depto','propietario','poseedor')

class EstacionamientoAdmin(admin.ModelAdmin):
	list_display = ('ubicacion',)

admin.site.register(Banco, BancoAdmin)
admin.site.register(TipoCuenta, TipoCuentaAdmin)
admin.site.register(TipoMovimiento, TipoMovimientoAdmin)
admin.site.register(Situacion, SituacionAdmin)
admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Condomino, CondominoAdmin)
admin.site.register(Estacionamiento, EstacionamientoAdmin)