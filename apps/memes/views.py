from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Meme, Comment
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    print(request.session['user_id'])
    print request.FILES
    all_data = Meme.objects.get_all_data(request.session['user_id'])
    context = {
        'data': all_data
    }
    print all_data['current_user'].username
    return render(request, 'memes/index.html', context)

def new_post(request):
    return render(request, 'memes/new_post.html')

def add_post(request):
    errors = Meme.objects.verify_post(request.POST, request.FILES)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('memes_ns:new_post')
    user_id = request.session['user_id']
    Meme.objects.add_post(request.POST, request.FILES, user_id)
    return redirect(reverse('memes_ns:index'))

def display_profile(request, user_id):
    print user_id
    user_posts = Meme.objects.get_user_posts(user_id)
    context = {'user_posts' : user_posts }
    return render(request, 'login_reg/profile.html', context)

def like_post(request, meme_id):
    user_id = request.session['user_id']
    Meme.objects.like_post(meme_id, user_id)
    return redirect('memes_ns:index')

def dislike_post(request, meme_id):
    user_id = request.session['user_id']
    Meme.objects.dislike_post(meme_id, user_id)
    return redirect('memes_ns:index')

def add_comment(request, meme_id):
    user_id = request.session['user_id']
    postData = request.POST
    fileData = request.FILES
    errors = Comment.objects.verify_comment(postData, fileData)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('memes_ns:index')
    Comment.objects.add_comment(postData, fileData, user_id, meme_id)
    return redirect('memes_ns:index')


#
# def add_meme_to_wl(request):
#     user_id = request.POST['user_id']
#     meme_id = request.POST['meme_id']
#     Meme.objects.add_to_wishlist(meme_id, user_id)
#     return redirect('memes_ns:index')
#
# def create_meme(request):
#     if len(request.POST['content']) < 3:
#         messages.add_message(request, messages.ERROR, 'Memes must be at least 3 characters long.')
#         return redirect('memes_ns:new_post')
#     Meme.objects.create_meme(request.POST, request.session['user_id'])
#     return redirect('memes_ns:index')
#
# def remove_meme(request):
#     meme_id = request.POST['meme_id']
#     user_id = request.POST['user_id']
#     Meme.objects.remove_from_wl(meme_id, user_id)
#     return redirect('memes_ns:index')
#
#
# def view_meme(request, meme_id):
#     memes_info = Meme.objects.get_meme_data(meme_id)
#     users = Meme.objects.get_meme_wishers(meme_id)
#     all_data = Meme.objects.get_all_data(request.session['user_id'])
#     context = {
#         'memes_data': memes_info,
#         'users': users,
#         'data': all_data
#     }
#     return render(request, 'memes/meme.html', context)
# def update_meme(request, meme_id):
#     Meme.objects.update_meme(request.POST, meme_id)
#     return redirect('/')
#
# def delete_meme(request, meme_id):
#     Meme.objects.delete_meme(request.POST, meme_id)
#     return redirect('/')
