from django.conf.urls import patterns, url

from qualifications import views

urlpatterns = patterns('', 
    #ex: /projects/
    url(r'^$', views.index, name='index'),
)