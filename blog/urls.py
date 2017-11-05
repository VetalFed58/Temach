from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
  # url(r'^$', views.post_list, name='post_list'),
    url(r'^post/$', views.post, name='post'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'blog:login'}, name='logout'),
    url(r'^new_post/$', views.load_new_fixtures),
    url(r'^$', views.main_page, name='home'),
    url(r'^post/(?P<post_id>\d+)/$', views.post),

]
#name="post_list"