from django.conf.urls.defaults import patterns, include, url
from encurtador.views import HomeTemplateView, GoToRedirectView, MyLinksListView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^(?P<uuid_curto>[\-\d\w]+)$', GoToRedirectView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^users/*', 'django.views.generic.simple.redirect_to', {'url': '/user/my-links/'}),
    url(r'^user/my-links/', MyLinksListView.as_view(), name='my_links'),
    (r'^user/accounts/', include('registration.backends.simple.urls')),
    (r'^user/auth/', include('registration.auth_urls')),
)
