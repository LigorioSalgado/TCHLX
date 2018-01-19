from django.conf.urls import url
from django.contrib import admin
from .views import index,post


urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^posts/(?P<slug>[\w-]+)/$', post,name="post"),
    
]