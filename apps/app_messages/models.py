from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User


class MessageManager(models.Manager):
    def create_thread(self, sender, receiver):
        Thread.create()
        return Thread.objects.get().latest('id')

    def create_message(self, sender, receiver, thread_id):
        pass






class Thread(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    content = models.TextField()
    sent_by = models.ForeignKey(User, related_name='messages_sent')
    received_by = models.ForeignKey(User, related_name='messages_received')
    thread_id = models.ForeignKey(Thread, related_name='thread_messages')
    viewed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
