from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$', views.index, name='index'),
	url('profile/$', views.userProfile, name='profile'),
]