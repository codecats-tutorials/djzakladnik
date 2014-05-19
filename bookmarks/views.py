from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from bookmarks.forms import UserForm
from bookmarks.models import Details, Bookmarks


def index(request):

    return render(request, 'bookmarks/index.html')

def add(request):
    detail = Details.objects.get(user_id = request.user.id)
    # bookmark = Bookmarks(url = 'http://onet.pl')
    # bookmark.author = detail
    # bookmark.save()
    # bookmark.subscribers.add(detail)
    # print detail
    return render(request, 'bookmarks/add.html')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            details = Details()
            details.user = user
            details.save()

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