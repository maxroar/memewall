from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_reg(self, postData):
        # list to hold error messages
        errors = []
        if not len(postData['username']) > 2:
            errors.append('User Name must be at least 3 characters.')
        if not len(postData['pass1']) > 7:
            errors.append('Password must be at least 8 characters.')
        if not postData['pass1'] == postData['pass2']:
            errors.append('Passwords must match.')
        if not self.check_username(postData):
            errors.append('User Name already in use.')
        return errors

    def check_username(self, postData):
        usernames = User.objects.filter(username=postData['username'])
        if usernames:
            return False
        return True

    def create_user(self, postData):
        User.objects.create(first_name=postData['first_name'], username=postData['username'], password=bcrypt.hashpw(postData['pass1'].encode(), bcrypt.gensalt()))

    def login(self, postData):
        user_data = User.objects.filter(username=postData['username']).first()
        # print(user_obj)
        pwhash = user_data.password.encode()
        if pwhash == bcrypt.hashpw(postData['pass1'].encode(), pwhash):
            return True
        return False

    def set_session(self, postData):
        user_data = User.objects.filter(username=postData['username']).first()
        user_id = user_data.id
        return user_id

    def get_user_data_from_session(self, session_id):
        user_data = User.objects.filter(id=session_id).first()
        print(user_data)
        return user_data


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=55)
    profile_pic = models.ImageField(upload_to='images', null=True, blank=True, height_field='height_field', width_field='width_field')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
