from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^create_meme$', views.create_meme, name='create_meme'),
    # url(r'^view_meme/(?P<meme_id>\d+)$', views.view_meme, name='view_meme'),
    # url(r'^update_meme/(?P<meme_id>\d+)$', views.update_meme, name='update_meme'),
    # url(r'^delete_meme/(?P<meme_id>\d+)$', views.delete_meme, name='delete_meme'),
    # url(r'^display_add_meme$', views.display_add_meme, name='display_add_meme'),
    # url(r'^remove_meme$', views.remove_meme, name='remove_meme'),
    # url(r'^add_meme_to_wl$', views.add_meme_to_wl, name='add_meme_to_wl'),
]
