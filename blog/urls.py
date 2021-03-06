from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^post/$', views.post, name='post'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'blog:login'}, name='logout'),
    url(r'^new_post_football/$', views.load_new_fixtures),
    url(r'^$', views.main_page, name='home'),
    url(r'^post/(?P<post_id>\d+)/$', views.post),
    url(r'^create_post/$', views.create_post),
    url(r'^football/$', views.football_page),
    url(r'^technologies/$', views.technologies_page),
    url(r'^userposts/$', views.userposts_page),
]