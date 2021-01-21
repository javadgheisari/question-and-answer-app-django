from django import forms
from .models import Profile

messages = {
    'required': 'این فیلد اجباری است',
    'invalid': 'لطفا یک ایمیل معتبر وارد کنید'
}


class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری', error_messages=messages, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control', 'placeholder': 'username'
                               }))

    password = forms.CharField(label='رمز عبور', error_messages=messages, max_length=35,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control', 'placeholder': 'password'
                               }))


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری', error_messages=messages, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control', 'placeholder': 'Username'
                               }))

    email = forms.EmailField(label='ایمیل', error_messages=messages, max_length=50,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control', 'placeholder': 'Email'
                             }))

    password = forms.CharField(label='رمز عبور', error_messages=messages, max_length=35,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control', 'placeholder': 'Password'
                               }))


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(label='ایمیل من', error_messages=messages, widget=forms.EmailInput(
        attrs={'style': 'width: 20em'}
    ))

    class Meta:
        model = Profile
        fields = ('bio', 'age')
        labels = {
            'bio': 'درباره من',
            'age': 'سن من'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:30em'})
        }
