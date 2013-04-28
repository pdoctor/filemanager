from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fm/', include('fm.urls',namespace="filemanager")),
    url(r'^accounts/', include('accounts.urls',namespace="accounts")),
    url(r'^users/', include('users.urls', namespace="users")),
)
