from django.conf.urls.defaults import patterns, include, url
from encurtador.views import HomeTemplateView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    # url(r'^dshortener/', include('dshortener.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^auth/', include('registration.auth_urls')),
)
