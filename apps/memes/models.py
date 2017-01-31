from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User
from stdimage.models import StdImageField

# Create your models here.
class MemeManager(models.Manager):
    def index(self, session_id):
        User.objects.get(id=session_id)
    # def create_meme(self, postData, user_id):
    #     user_name=User.objects.get(id=user_id)
    #     self.create(name=postData['content'], user=User.objects.get(id=user_id), added_by=user_name.first_name)
    #     meme_id = self.filter().latest('id')
    #     self.add_to_wishlist(meme_id.id, user_id)
    #
    # def add_to_wishlist(self, meme_id, user_id):
    #     meme_obj = self.get(id=meme_id)
    #     meme_obj.wishlist.add(user_id)
    #
    # def get_all_data(self, user_id):
    #     user_data = User.objects.all()
    #     memes_data = self.all()
    #     current_user = User.objects.get_user_data_from_session(user_id)
    #     other_memes = self.get_other_memes(user_id)
    #     all_data = {
    #         'users': user_data,
    #         'memes': memes_data,
    #         'current_user': current_user,
    #         'other_memes': other_memes
    #     }
    #     print all_data
    #     return all_data
    #
    # def get_wishlist(self, user_id):
    #     return self.filter(wishlist__id=user_id)
    #
    # def get_other_memes(self, user_id):
    #     return self.all().exclude(wishlist__id=user_id)
    #
    # def remove_from_wl(self, meme_id, user_id):
    #     meme_obj = self.get(id=meme_id)
    #     user_obj = User.objects.get(id=user_id)
    #     meme_obj.wishlist.remove(user_obj)
    #
    # def get_meme_wishers(self, meme_id):
    #     users = User.objects.filter(in_wishlist=meme_id)
    #     print users
    #     return users
    #
    # def get_meme_data(self, meme_id):
    #     meme_data = self.get(id=meme_id)
    #     print meme_data
    #     return meme_data
    #
    # def is_user(self, meme_id, user_id):
    #     is_true = self.filter(id=meme_id,user=User.objects.get(id=user_id))
    #     return is_true
    #
    # def update_meme(self, postData, meme_id):
    #     content=postData['content']
    #     self.filter(id=meme_id).update(content=content)
    #
    # def delete_meme(self, postData, meme_id):
    #     self.filter(id=meme_id).delete()
    #     # one time user
    #     self.objects.all().delete()
    #     User.objects.all().delete()


class Meme(models.Model):
    choices = (
        ('f', 'funny'),
        ('p', 'politics'),
        ('r', 'reality')
    )

    meme = StdImageField(upload_to='images/', null=True, blank=True, variations={
        'large': (400, 400),
        'thumbnail': (100, 100, True),
        'medium': (250, 250),
    })
    title = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, related_name='added_memes')
    categories = models.CharField(max_length=1, choices=choices)
    likes = models.ManyToManyField(User, related_name='liked_memes', null=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_memes', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MemeManager()
