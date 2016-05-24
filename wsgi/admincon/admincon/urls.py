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
from django.contrib.auth.views import login,logout

admin.autodiscover()

from main.views import CondominoViewSet

urlpatterns = [
    url(r'^accounts/login/$' , login , {'template_name':'home/login.html'} ),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
    url(r'^api-rest/(?P<mail_id>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',CondominoViewSet.as_view(),name='my_rest_view'),
    url(r'^$', 'main.views.home'),
    url(r'^bancos/', 'main.views.banco_list'),
    url(r'^condominios/', 'main.views.condominio_list'),
    url(r'^pagos/', 'main.views.pago_depto_list'),
    url(r'^movtos/', 'main.views.movtos_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^explorer/', include('explorer.urls')),
]
