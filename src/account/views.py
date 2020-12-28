from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # یک دیکشنری از اطلاعات فرم را برمیگرداند
            user = authenticate(request, username=cd['username'], password=cd['password'])
            # احراز هویت را انجام میدهد
            if user is not None:
                login(request, user)
                messages.success(request, 'you are registered', 'success')
                return redirect('posts:all_posts')

            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است', 'danger')
    else:
        form = UserLoginForm()

    return render(request, 'account/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            # ساخت کاربر و ثبت نام آن
            login(request, user)
            # پس از ثبت نام مستقیم لاگین کند
            messages.success(request, 'با موفقیت ثبت نام شدید', 'success')
            return redirect('posts:all_posts')

    else:
        form = UserLoginForm()

    return render(request, 'account/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید', 'success')
    return redirect('posts:all_posts')
