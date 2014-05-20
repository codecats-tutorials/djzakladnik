from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from bookmarks.forms import UserForm, BookmarkForm
from bookmarks.models import Profile, Bookmark


def index(request):
    return render(request, 'bookmarks/index.html')

def my(request):
    profile = Profile.objects.get(user_id = request.user.id)
    bookmarks = profile.bookmark_set.all()

    return render(request, 'bookmarks/my.html', {
        'bookmarks': bookmarks
    })

def add(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit = False)
            profile = Profile.objects.get(user_id = request.user.id)
            bookmark.author = profile
            bookmark.save()
            bookmark.subscribers.add(profile)

    else:
        form = BookmarkForm()

    return render(request, 'bookmarks/add.html', {
        'form' : form
    })

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            profile = Profile()
            profile.user = user
            profile.save()

            return redirect(reverse('bookmarks:index'))
    else:
        form = UserForm()

    return render(request, 'registration/registration.html', {
        'form' : form
    })

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username = username, password = password)
    if user is not None and user.is_active:
        auth.login(request, user)

        return redirect(reverse('bookmarks:index'))

    return render(request, 'bookmarks/login.html')