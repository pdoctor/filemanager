from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
	# ex: /accounts/
    url(r'^$', views.index, name='index'),

    # ex: /accounts/5/
    url(r'^(?P<account_id>\d+)/$', views.account_detail, name='account_detail'),

    # ex: /accounts/5/
    url(r'^new/$', views.add_account, name='account_add'),

 )