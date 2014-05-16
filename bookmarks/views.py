from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth

def index(request):

    print request.user.is_authenticated()
    #user = auth.authenticate(username = 's', password = 'tomek11')
    #print user.is_authenticated()
    return render(request, 'bookmarks/index.html')

# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#
#     user = auth.authenticate(username = username, password = password)
#     if user is not None and user.is_active:
#         auth.login(request, user)
#
#         return redirect(reverse('bookmarks:index'))
#
#     return render(request, 'bookmarks/login.html')
#
#
#
#
# def register(request):
#     return render(request, 'bookmarks/register.html')
#
# def logout(request):
#     auth.logout(request)
#
#     return redirect(reverse('bookmarks:index'))