from django.conf.urls import url
from layui import views

urlpatterns = [
        url(r'^$', views.hello_world, name='hello_world'),        
        url(r'^table/$', views.table, name='table'),        
        url(r'^json/$', views.json, name='json'),        
        url(r'^json2/$', views.json2, name='json2'),        
        url(r'^admintest/$', views.admintest, name='admintest'),        
        url(r'^all/$', views.all, name='all'),        
        url(r'^button/$', views.button, name='button'),        
        url(r'^form/$', views.form, name='form'),        
        url(r'^xingzuo/$', views.xingzuo, name='xingzuo'),        
        url(r'^form2/$', views.form2, name='form2'),        
        url(r'^posttest/$', views.posttest, name='posttest'),        
        ]

