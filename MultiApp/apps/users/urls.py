from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', login, {'template_name': 'users/login.html' }),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<user_id>\d+)$', views.show),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    url(r'^(?P<user_id>\d+)/delete$', views.delete)


]