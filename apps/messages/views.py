from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Message, Thread
from django.core.urlresolvers import reverse

def display_threads(request, user_id):
    pass
