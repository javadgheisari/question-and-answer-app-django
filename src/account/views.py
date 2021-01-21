from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from posts.models import Post
from django.contrib.auth.decorators import login_required


def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # یک دیکشنری از اطلاعات فرم را برمیگرداند
            user = authenticate(request, username=cd['username'], password=cd['password'])
            # احراز هویت را انجام میدهد
            if user is not None:
                login(request, user)
                messages.info(request, 'با موفقیت وارد شدید')
                if next:
                    return redirect(next)
                return redirect('posts:all_posts')

            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
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
            messages.success(request, 'با موفقیت ثبت نام شدید')
            return redirect('posts:all_posts')

    else:
        form = UserRegisterForm()

    return render(request, 'account/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید')
    return redirect('posts:all_posts')


@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    self_dash = False
    if request.user.id == user_id:
        self_dash = True
    return render(request, 'account/dashboard.html', {'user': user, 'posts': posts, 'self_dash': self_dash})


def all_account(request):
    users = User.objects.all()
    return render(request, 'account/all_account.html', {"users": users})
