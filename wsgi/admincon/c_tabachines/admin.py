from django.contrib import admin
from models import Condomino, Movimiento, Cuota, Recibo, Estacionamiento

class MovimientoAdminD(admin.ModelAdmin):
	list_display = ('id','fecha','tipo_movimiento','retiro','deposito','condomino')
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class CondominoAdminD(admin.ModelAdmin):
	list_display = ('depto','ubicacion','propietario','poseedor')
	search_fields = ('depto','propietario','poseedor')

class EstacionamientoAdminD(admin.ModelAdmin):
	list_display = ('ubicacion',)

class CuotaAdminD(admin.ModelAdmin):
	list_display = ('tipo_cuota','fecha_inicio','fecha_fin','monto', 'pago')
	list_filter = ('fecha_inicio',)
	date_hierarchy = 'fecha_inicio'
	ordering = ('-fecha_inicio',)

class ReciboAdminD(admin.ModelAdmin):
	list_display = ('folio','fecha','condomino','monto','situacion')
	search_fields = ('folio',)
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

admin.site.register(Movimiento, MovimientoAdminD)
admin.site.register(Condomino, CondominoAdminD)
admin.site.register(Estacionamiento, EstacionamientoAdminD)
admin.site.register(Recibo, ReciboAdminD)
admin.site.register(Cuota, CuotaAdminD)