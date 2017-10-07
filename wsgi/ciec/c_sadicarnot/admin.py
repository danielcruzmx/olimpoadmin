from django.contrib import admin
from models import Condomino, Movimiento, Cuota, Recibo, Estacionamiento

class MovimientoAdminC(admin.ModelAdmin):
	list_display = ('id','fecha','tipo_movimiento','retiro','deposito','condomino')
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class CondominoAdminC(admin.ModelAdmin):
	list_display = ('depto','ubicacion','propietario','poseedor')
	search_fields = ('depto','propietario','poseedor')

class EstacionamientoAdminC(admin.ModelAdmin):
	list_display = ('ubicacion',)

class CuotaAdminC(admin.ModelAdmin):
	list_display = ('condomino','tipo_cuota','fecha_inicio','fecha_fin','monto', 'pago')
	list_filter = ('fecha_inicio',)
	date_hierarchy = 'fecha_inicio'
	ordering = ('-fecha_inicio',)

class ReciboAdminC(admin.ModelAdmin):
	list_display = ('folio','fecha','condomino','monto','situacion')
	search_fields = ('folio',)
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

admin.site.register(Movimiento, MovimientoAdminC)
admin.site.register(Condomino, CondominoAdminC)
admin.site.register(Estacionamiento, EstacionamientoAdminC)
admin.site.register(Recibo, ReciboAdminC)
admin.site.register(Cuota, CuotaAdminC)