from django.conf.urls import url
from layui import views

urlpatterns = [
        url(r'^$', views.hello_world, name='hello_world'),        
        url(r'^table/$', views.table, name='table'),        
        url(r'^json/$', views.json, name='json'),        
        ]

