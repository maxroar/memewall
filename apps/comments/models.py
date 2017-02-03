from __future__ import unicode_literals
from django.db import models
from ..memes.models import Meme
from ..login_reg.models import User
from stdimage.models import StdImageField

# Create your models here.
class CommentManager(models.Manager):
    # def index(self, session_id):
    #     User.objects.get(id=session_id)
    # def create_meme(self, postData, user_id):
    #     user_name=User.objects.get(id=user_id)
    #     self.create(name=postData['content'], user=User.objects.get(id=user_id), added_by=user_name.first_name)
    #     meme_id = self.filter().latest('id')
    #     self.add_to_wishlist(meme_id.id, user_id)
    #
    def verify_comment(self, postData, imgFile):
        errors = []
        if not len(postData['comment_text']) > 0 or imgFile:
            errors.append('Please include either an image or a comment.')
        return errors



    def add_comment(self, postData, imgFile, user_id, meme_id):
        user = User.objects.get(id=user_id)
        meme = Meme.objects.get(id=meme_id)
        if not imgFile:
            self.create(
                comment_text=postData['comment_text'],
                added_by=user,
                meme_post=meme
            )
        elif len(postData['comment_text']) == 0:
            self.create(
                comment_pic=imgFile['comment_pic'],
                added_by=user,
                meme_post=meme
            )
        else:
            self.create(
                comment_text=postData['comment_text'],
                comment_pic=imgFile['comment_pic'],
                added_by=user,
                meme_post=meme
            )

    # make a query to return errthang the user has touched as the post only


    # def get_user_posts(self, user_id):
    #     user = User.objects.get(id=user_id)
    #     memes = self.filter(added_by=user).order_by('-created_at')
    #     return memes
    #
    # def like_post(self, meme_id, user_id):
    #     user = User.objects.get(id=user_id)
    #     meme = self.get(id=meme_id)
    #     if not user in meme.likes.all():
    #         meme.likes.add(user)
    #         return 0
    #     meme.likes.remove(user)
    #
    #
    # def dislike_post(self, meme_id, user_id):
    #     user = User.objects.get(id=user_id)
    #     meme = self.get(id=meme_id)
    #     if not user in meme.likes.all():
    #         meme.dislikes.add(user)
    #         return 0
    #     meme.likes.remove(user)
    #
    # # def get_other_memes(self, user_id):
    # #     return self.all().exclude(wishlist__id=user_id)
    # #
    # # def remove_from_wl(self, meme_id, user_id):
    # #     meme_obj = self.get(id=meme_id)
    # #     user_obj = User.objects.get(id=user_id)
    # #     meme_obj.wishlist.remove(user_obj)
    # #
    # # def get_meme_wishers(self, meme_id):
    # #     users = User.objects.filter(in_wishlist=meme_id)
    # #     print users
    # #     return users
    # #
    # # def get_meme_data(self, meme_id):
    # #     meme_data = self.get(id=meme_id)
    # #     print meme_data
    # #     return meme_data
    # #
    # # def is_user(self, meme_id, user_id):
    # #     is_true = self.filter(id=meme_id,user=User.objects.get(id=user_id))
    # #     return is_true
    # #
    # # def update_meme(self, postData, meme_id):
    # #     content=postData['content']
    # #     self.filter(id=meme_id).update(content=content)
    # #
    # # def delete_meme(self, postData, meme_id):
    # #     self.filter(id=meme_id).delete()
    # #     # one time user
    # #     self.objects.all().delete()
    # #     User.objects.all().delete()


class Comment(models.Model):
    comment_pic = StdImageField(upload_to='images/', null=True, blank=True, variations={
        'large': (400, 400),
        'thumbnail': (100, 100, True),
        'medium': (250, 250),
        'icon': (40, 40, True)
    })
    comment_text = models.TextField(null=True)
    meme_post = models.ForeignKey(Meme, related_name='meme_comments')
    added_by = models.ForeignKey(User, related_name='added_comments')
    likes = models.ManyToManyField(User, related_name='liked_comments', null=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()
