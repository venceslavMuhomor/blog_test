from django import forms
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category']
        widgets = {
            'category': forms.Select(attrs={'type': 'text', 'name':'name', 'placeholder': 'категория'})
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']