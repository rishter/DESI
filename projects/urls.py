from django.conf.urls import patterns, url

from projects import views

urlpatterns = patterns('', 
    #ex: /projects/
    url(r'^$', views.index, name='index'),
    #ex: /projects/5/
    url(r'^(?P<proj_name_short>\w+)/$', views.detail, name='detail'),
)