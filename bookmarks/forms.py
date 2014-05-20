# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from bookmarks.models import Bookmark

class BookmarkForm(forms.ModelForm):
    url = forms.URLField(required = True)
    title = forms.Field(required = False)
    class Meta:
        model = Bookmark
        fields = ['url', 'title', 'description']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            raise forms.ValidationError("Hasło musi być potwierdzone")

        return self.cleaned_data
