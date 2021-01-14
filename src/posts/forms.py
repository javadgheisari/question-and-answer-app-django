from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'category')
        labels = {
            'body': 'بدنه',
            'category': 'دسته بندی'
        }
