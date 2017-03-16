from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User

# Create your models here.
class MessageManager(models.Manager):

    def verify_message(self, postData):
        errors = []
        if not len(postData['message_text']) > 0:
            errors.append('Please include a message.')
        return errors

    def get_all_threads(self, user_id):
        memes_data = Meme.objects.order_by('-created_at')
        current_user = User.objects.get_user_data_from_session(user_id)
        comments = Comment.objects.all()
        # other_memes = self.get_other_memes(user_id)
        all_data = {
            # 'users': user_data,
            'memes': memes_data,
            'current_user': current_user,
            'comments': comments
        }
        print (current_user)
        return all_data

    def add_post(self, postData, imgFile, user_id):
        user = User.objects.get(id=user_id)
        self.create(
            title=postData['post_title'],
            meme=imgFile['meme_post'],
            category=postData['category'],
            added_by=user
        )

    def get_user_posts(self, user_id):
        user = User.objects.get(id=user_id)
        memes = self.filter(added_by=user).order_by('-created_at')
        return memes

    def like_post(self, meme_id, user_id):
        user = User.objects.get(id=user_id)
        meme = self.get(id=meme_id)
        if not user in meme.likes.all():
            meme.likes.add(user)
            return 0
        meme.likes.remove(user)

    def dislike_post(self, meme_id, user_id):
        user = User.objects.get(id=user_id)
        meme = self.get(id=meme_id)
        if not user in meme.dislikes.all():
            meme.dislikes.add(user)
            return 0
        meme.dislikes.remove(user)


class CommentManager(models.Manager):

    def verify_comment(self, postData, imgFile):
        errors = []
        if not len(postData['comment_text']) > 0 and not imgFile:
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


class Message(models.Model):
    message_text = models.CharField(max_length=200)
    sent_by = models.ForeignKey(User, related_name='sent_messages')
    received_by = models.ForeignKey(User, related_name='received_messages')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = MessageManager()
