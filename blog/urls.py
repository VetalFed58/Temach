from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  # url(r'^$', views.post_list, name='post_list'),
    url(r'^post/$', views.post, name='post'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'blog:login'}, name='logout'),
]
#name="post_list"