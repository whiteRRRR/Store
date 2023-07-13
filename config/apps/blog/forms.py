from django.forms import ModelForm
from .models import CommentBlog
from django import forms


class CommentForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control w-100',
               'rows': 9,
               'placeholder': 'Write Comment'}))

    class Meta:
        model = CommentBlog
        fields = ('content', )


