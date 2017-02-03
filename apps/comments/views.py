from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment, CommentManager
from django.core.urlresolvers import reverse

def index(request):
    # do stuff in models
    return redirect('memes_ns:index')
