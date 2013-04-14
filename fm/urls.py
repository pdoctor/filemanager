from django.conf.urls import patterns, url

from fm import views

urlpatterns = patterns('',
	# ex: /fm/
    url(r'^$', views.index, name='index'),
    # ex: /fm/manage_document/
    url(r'^manage_document/$', views.manage_document, name='manage_document'),    
    # ex: /fm/5/
    url(r'^(?P<document_id>\d+)/$', views.detail, name='detail'),
    # ex: /download/5/
    url(r'^download/(?P<document_id>\d+)/$', views.download, name='download'),
 )