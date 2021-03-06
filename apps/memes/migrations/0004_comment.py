# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 23:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0002_auto_20170131_0556'),
        ('memes', '0003_auto_20170202_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_pic', stdimage.models.StdImageField(blank=True, null=True, upload_to='images/')),
                ('comment_text', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_comments', to='login_reg.User')),
                ('dislikes', models.ManyToManyField(null=True, related_name='disliked_comments', to='login_reg.User')),
                ('likes', models.ManyToManyField(null=True, related_name='liked_comments', to='login_reg.User')),
                ('meme_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meme_comments', to='memes.Meme')),
            ],
        ),
    ]
