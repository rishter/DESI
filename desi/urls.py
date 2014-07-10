from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'desi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'all.views.index', name='home'),
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^qualifications/', include('qualifications.urls', namespace="qualifications")),
    url(r'^clients/', include('clients.urls', namespace="clients")),
    url(r'^about/', include('about.urls', namespace="about")),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^careers/', include('careers.urls', namespace='careers')),
)
