from django.conf.urls import url
from django.views.generic import ListView, DetailView
from loan.models import Post
from django.urls import path


urlpatterns = [
	url('^$', ListView.as_view(queryset=Post.objects.order_by('-date')[:25], template_name='loan/post.html')),
	url('^(?P<pk>\d+)$', DetailView.as_view(model = Post , template_name = 'loan/detail.html')),
	
]