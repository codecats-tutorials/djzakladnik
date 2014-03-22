from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth


def index(request):
    return render(request, 'bookmarks/index.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is None:
        return render(request, 'bookmarks/login.html')

    return redirect(reverse('bookmarks:index'))


def register(request):
    return render(request, 'bookmarks/register.html')