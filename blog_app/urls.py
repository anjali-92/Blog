from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^post/list/$', views.post_list, name='post_list'),
            url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
            url(r'^post/new/$', views.new_post, name='new_post'),
            url(r'^post/(?P<pk>\d+)/edit/$', views.edit_post, name='edit_post'),
            ]
