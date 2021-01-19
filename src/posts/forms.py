from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'category')
        labels = {
            'body': 'بدنه',
            'category': 'دسته بندی'
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'category')
        labels = {
            'body': 'بدنه',
            'category': 'دسته بندی'
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }
