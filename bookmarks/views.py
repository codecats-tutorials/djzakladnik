from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from bookmarks.forms import UserForm, BookmarkForm
from bookmarks.models import Profile, Bookmark


def index(request):
    bookmarks = Bookmark.objects.all()
    subscribedBookmarks = None
    try:
        profile = Profile.objects.get(user_id = request.user.id)
        subscribedBookmarks = Bookmark.objects.filter(subscribers = profile)
    except:
        profile = None

    return render(request, 'bookmarks/index.html', {
        'bookmarks': bookmarks,
        'subscribedBookmarks': subscribedBookmarks
    })

def subscribe(request, id):
    profile = Profile.objects.get(user_id = request.user.id)
    bookmark = Bookmark.objects.get(pk=id)
    bookmark.subscribers.add(profile)

    return redirect(reverse('bookmarks:index'))

def unsubscribe(request, id):
    profile = Profile.objects.get(user_id = request.user.id)
    bookmark = Bookmark.objects.get(pk=id)
    bookmark.subscribers.remove(profile)

    return redirect(reverse('bookmarks:my'))

def my(request):
    profile = Profile.objects.get(user_id = request.user.id)
    bookmarks = Bookmark.objects.filter(subscribers = profile)

    return render(request, 'bookmarks/my.html', {
        'bookmarks': bookmarks
    })

def add(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = Bookmark.objects.get(url=form.cleaned_data['url'])
            profile = Profile.objects.get(user_id = request.user.id)
            if bookmark is None:
                bookmark = form.save(commit = False)
                bookmark.author = profile
                bookmark.save()
            bookmark.subscribers.add(profile)

            return redirect(reverse('bookmarks:index'))
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