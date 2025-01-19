from django import forms
from .models import Userinfo, Post

class UserForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['username', 'email', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'body', 'status']