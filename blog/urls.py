from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

# Traditionally we'd also need to modify the blog/views.py before being done but we can skip that part entirely with some generic views
# ListView used mainly for a page that presents a list of something to the user
# Rather than writing a SQL-specific statement, we just reference our model. Django knows how to build the query in the background

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name="blog/post.html")),
]