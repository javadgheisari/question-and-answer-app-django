from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import AddPostForm, EditPostForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', {'posts': posts})


# ---------------------category views---------------------------------
def post_darsi(request):
    posts = Post.objects.all()
    return render(request, 'posts/category/darsi.html', {'posts': posts})


def post_eghtesadi(request):
    posts = Post.objects.all()
    return render(request, 'posts/category/eghtesadi.html', {'posts': posts})


def post_ejtemaei(request):
    posts = Post.objects.all()
    return render(request, 'posts/category/ejtemaei.html', {'posts': posts})


def post_farhango_honar(request):
    posts = Post.objects.all()
    return render(request, 'posts/category/farhango honar.html', {'posts': posts})


def post_siyasi(request):
    posts = Post.objects.all()
    return render(request, 'posts/category/siyasi.html', {'posts': posts})


# -------------------------------------------------------------------------------

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, created__year=year, created__month=month, created__day=day,
                             slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def add_post(request, user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.slug = slugify(form.cleaned_data['body'][:20], allow_unicode=True)
                new_post.save()
                messages.success(request, 'پرسش شما ثبت شد')
                return redirect('account:dashboard', user_id)
        else:
            form = AddPostForm()
            return render(request, 'posts/add_post.html', {'form': form})
    else:
        return redirect('posts:all_posts')


def post_delete(request, user_id, post_id):
    if user_id == request.user.id:
        Post.objects.filter(id=post_id).delete()
        messages.success(request, 'پرسش شما با موفقیت حذف شد')
        return redirect('account:dashboard', user_id)
    else:
        return redirect('posts:all_posts')


@login_required
def post_edit(request, user_id, post_id):
    if request.user.id == user_id:
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                ep = form.save(commit=False)
                ep.slug = slugify(form.cleaned_data['body'][:20], allow_unicode=True)
                ep.save()
                messages.success(request, 'پرسش شما با موفقیت ویرایش شد')
                return redirect('account:dashboard', user_id)
        else:
            form = EditPostForm(instance=post)
        return render(request, 'posts/edit_post.html', {'form': form})
    else:
        return redirect('posts:all_posts')
