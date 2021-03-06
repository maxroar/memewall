from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        messages.add_message(request, messages.ERROR, 'You were already logged in, goof. If you would like to log into or register a new account, please log out first.')
        print('logged in')
        return redirect(reverse('memes_ns:index'))
    return render(request, 'login_reg/index.html')
def register(request):
    errors = User.objects.validate_reg(request.POST, request.FILES)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('login_ns:index')

    user_data = User.objects.create_user(request.POST, request.FILES)

    request.session['user_id'] = User.objects.set_session(request.POST)
    return redirect(reverse('memes_ns:index'))
def login(request):
    is_username = User.objects.check_username(request.POST)
    if is_username:
         messages.error(request, 'This user name has not been registered.')
         return redirect('login_ns:index')
    is_match = User.objects.login(request.POST)
    if not is_match:
        messages.error(request, 'The username or password is incorrect.')
        return redirect('login_ns:index')
    request.session['user_id'] = User.objects.set_session(request.POST)
    return redirect(reverse('memes_ns:index'))



    # make a method to get user_data from session
    # make a method to get get a join query of user posts + user comments and sort by descending chronological order w/ datetime
    # pass each in context as individual keys


def logout(request):
    request.session.flush()
    return redirect('/')
