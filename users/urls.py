from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
	# ex: /users/
    url(r'^$', views.index, name='index'),

    # ex: /users/login/
    url(r'^login/$', views.login_user, name='user_login'),

    # ex: /users/logout/
    url(r'^logout/$', views.logout_user, name='logout_user'),

 )