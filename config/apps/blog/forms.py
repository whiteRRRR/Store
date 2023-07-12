from django.forms import ModelForm
from .models import CommentBlog


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['email'].disabled = True

    class Meta:
        model = CommentBlog
        fields = ['name', 'email', 'body']