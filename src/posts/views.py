from django.shortcuts import render, get_object_or_404
from .models import Post


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
