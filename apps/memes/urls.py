from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_post$', views.new_post, name='new_post'),
    # url(r'^view_meme/(?P<meme_id>\d+)$', views.view_meme, name='view_meme'),
    url(r'^display_profile/(?P<user_id>\d+)$', views.display_profile, name='display_profile'),
    # url(r'^update_meme/(?P<meme_id>\d+)$', views.update_meme, name='update_meme'),
    url(r'^like_post/(?P<meme_id>\d+)$', views.like_post, name='like_post'),
    url(r'^dislike_post/(?P<meme_id>\d+)$', views.dislike_post, name='dislike_post'),
    url(r'^add_post$', views.add_post, name='add_post'),
    url(r'^add_comment/(?P<meme_id>\d+)$', views.add_comment, name='add_comment'),
    # url(r'^remove_meme$', views.remove_meme, name='remove_meme'),
    # url(r'^add_meme_to_wl$', views.add_meme_to_wl, name='add_meme_to_wl'),
]
