"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from django.views.generic import RedirectView
from django.contrib.auth.views import login,logout

admin.autodiscover()

#from main.views import CondominoViewSet
from main.views import CuotasViewSet
from main.views import CondominosOlimpoViewSet
from main.views import FaltantesMesOlimpoViewSet, \
                       CuotasDeptoMesOlimpoViewSet, \
                       MovimientosOlimpoViewSet, \
                       NoIdentificadosOlimpoViewSet, \
                       TotalIngresosEgresosOlimpoViewSet

urlpatterns = [
    url(r'^accounts/login/$' , login , {'template_name':'home/login.html'} ),
    url(r'^accounts/logout/$', logout, {'next_page': '/home/login.html'}),
    #url(r'^api-rest/(?P<mail_id>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',CondominoViewSet.as_view(),name='my_rest_view'),
    #url(r'^admin/report/cuotas/(\w+)/(\d+)/$', 'main.views.reporte_adeudos'),
    #url(r'^api-rest/movimientos/(?P<depto_id>[\w]+)/$',
    #   CuotasViewSet.as_view(),
    #    name='my_rest_view'),
    url(r'^api-rest/olimpo/informe/(?P<depto_id>[\w]+)/$',
        CuotasViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/olimpo/condominos/$',
        CondominosOlimpoViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/olimpo/faltantesMes/(?P<mes_anio>(0?[1-9]|1[012])-((19|20)\d\d))/$',
        FaltantesMesOlimpoViewSet.as_view(),
        name='my_rest_view'),
    url(r'^api-rest/olimpo/cuotasDeptoMes/(?P<mes_anio>(0?[1-9]|1[012])-((19|20)\d\d))/$',
        CuotasDeptoMesOlimpoViewSet.as_view(),
        name='my_rest_view'),
    url(
        r'^api-rest/olimpo/movimientos/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
        MovimientosOlimpoViewSet.as_view(),
        name='my_rest_view'),
    url(
        r'^api-rest/olimpo/noIdentificados/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
        NoIdentificadosOlimpoViewSet.as_view(),
        name='my_rest_view'),
    url(
        r'^api-rest/olimpo/totalIngresosEgresos/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
        TotalIngresosEgresosOlimpoViewSet.as_view(),
        name='my_rest_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home'),
    url(r'^queries/', 'main.views.query_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^explorer/', include('explorer.urls')),
]
