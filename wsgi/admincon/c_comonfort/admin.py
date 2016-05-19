from django.contrib import admin
from models import Condomino, Movimiento, Cuota, Recibo, Estacionamiento

class MovimientoAdminA(admin.ModelAdmin):
	list_display = ('id','fecha','tipo_movimiento','retiro','deposito','condomino')
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class CondominoAdminA(admin.ModelAdmin):
	list_display = ('depto','ubicacion','propietario','poseedor')
	search_fields = ('depto','propietario','poseedor')

class EstacionamientoAdminA(admin.ModelAdmin):
	list_display = ('ubicacion',)

class CuotaAdminA(admin.ModelAdmin):
	list_display = ('tipo_cuota','fecha_inicio','fecha_fin','monto', 'pago')
	list_filter = ('fecha_inicio',)
	date_hierarchy = 'fecha_inicio'
	ordering = ('-fecha_inicio',)

class ReciboAdminA(admin.ModelAdmin):
	list_display = ('folio','fecha','condomino','monto','situacion')
	search_fields = ('folio',)
	list_filter = ('fecha',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

admin.site.register(Movimiento, MovimientoAdminA)
admin.site.register(Condomino, CondominoAdminA)
admin.site.register(Estacionamiento, EstacionamientoAdminA)
admin.site.register(Recibo, ReciboAdminA)
admin.site.register(Cuota, CuotaAdminA)