from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Meme
# Create your views here.
def index(request):
    print(request.session['user_id'])
    # all_data = Meme.objects.get_all_data(request.session['user_id'])
    # context = {
    #     'data': all_data
    # }
    # print(all_data['wishlist'])
    return render(request, 'memes/index.html')

# def display_add_meme(request):
#     all_data = Meme.objects.get_all_data(request.session['user_id'])
#     context = {
#         'data': all_data
#     }
#     return render(request, 'memes/add_meme.html', context)
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
#         return redirect('memes_ns:display_add_meme')
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
