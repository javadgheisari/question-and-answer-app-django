from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'category')
        labels = {
            'body': '',
            'category': 'دسته بندی'
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'بپرسید ...'})
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'category')
        labels = {
            'body': '',
            'category': 'دسته بندی'
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'بنویسید ...'})
        }


class AddReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'row': 1, 'style': 'height: 5em;'})
        }
