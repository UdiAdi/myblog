from django.shortcuts import get_object_or_404
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from userprofile.models import User
from . import views

app_name = 'userprofile'

urlpatterns = [
	#/userprofile/login
	url(r'^login$', views.login_view, name="login"),

	#/userprofile/posts
	url(r'^posts/$', views.userposts, name="userposts"),

	# #/userprofile/register
	# url(r'^register/$', views.register_view, name="register"),

	#/userprofile/1/
    url (r'^(?P<pk>\d+)/$', DetailView.as_view(model=User, template_name='userprofile/userprofile.html'), name="userinfo"),
   ]
#url(r'^(?P<pk>\d+)/$', views.info_view, name="userinfo", <pk>)