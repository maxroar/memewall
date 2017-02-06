from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^display_messages/(?P<user_id>\d+)$', views.display_messages, name='display_messages'),
    # url(r'^update_meme/(?P<meme_id>\d+)$', views.update_meme, name='update_meme'),
    url(r'^display_thread/(?P<thread_id>\d+)$', views.display_thread, name='display_thread'),
    # url(r'^dislike_post/(?P<meme_id>\d+)$', views.dislike_post, name='dislike_post'),
    # url(r'^add_post$', views.add_post, name='add_post'),
    # url(r'^add_comment/(?P<meme_id>\d+)$', views.add_comment, name='add_comment'),
    # url(r'^remove_meme$', views.remove_meme, name='remove_meme'),
    # url(r'^add_meme_to_wl$', views.add_meme_to_wl, name='add_meme_to_wl'),
]
