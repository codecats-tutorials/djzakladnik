from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from bookmarks.forms import UserForm


def index(request):

    print request.user.is_authenticated()
    #user = auth.authenticate(username = 's', password = 'tomek11')
    #print user.is_authenticated()
    return render(request, 'bookmarks/index.html')

def registration(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            return redirect(reverse('bookmarks:index'))
    else:
        form = UserForm()

    return render(request, 'registration/registration.html', {
        'form' : form
    })

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