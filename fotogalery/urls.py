import django.conf.urls
from django.contrib import admin


admin.autodiscover()

urlpatterns = django.conf.urls.patterns('',
    # Examples:
    # url(r'^$', 'fotogalery.views.home', name='home'),
    # url(r'^fotogalery/', include('fotogalery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    django.conf.urls.url(r'^admin/doc/', django.conf.urls.include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    django.conf.urls.url(r'^admin/', django.conf.urls.include(admin.site.urls)),
)
