from django.contrib import admin
from models import Condomino, Movimiento, Cuota, Recibo, Estacionamiento

class MovimientoAdminB(admin.ModelAdmin):
	list_display = ('id','fecha','tipo_movimiento','retiro','deposito','condomino')
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class CondominoAdminB(admin.ModelAdmin):
	list_display = ('depto','ubicacion','propietario','poseedor')
	search_fields = ('depto','propietario','poseedor')

class EstacionamientoAdminB(admin.ModelAdmin):
	list_display = ('ubicacion',)

class CuotaAdminB(admin.ModelAdmin):
	list_display = ('tipo_cuota','fecha_inicio','fecha_fin','monto', 'pago')
	list_filter = ('fecha_inicio',)
	date_hierarchy = 'fecha_inicio'
	ordering = ('-fecha_inicio',)

class ReciboAdminB(admin.ModelAdmin):
	list_display = ('folio','fecha','condomino','monto','situacion')
	search_fields = ('folio',)
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

admin.site.register(Movimiento, MovimientoAdminB)
admin.site.register(Condomino, CondominoAdminB)
admin.site.register(Estacionamiento, EstacionamientoAdminB)
admin.site.register(Recibo, ReciboAdminB)
admin.site.register(Cuota, CuotaAdminB)