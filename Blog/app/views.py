from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render
from .models import Category
from app.models import Post


def index(request):
    popular_post = Post.objects.filter(
        section='Popular', status=1).order_by('-id')[0:4]
    recent_post = Post.objects.filter(
        section='Recent', status=1).order_by('-id')[0:4]
    Editors_Pick = Post.objects.filter(
        section='Editors_Pick', status=1).order_by('-id')
    Trending = Post.objects.filter(
        section='Trending', status=1).order_by('-id')[0:4]
    Inspiration = Post.objects.filter(
        section='Inspiration', status=1).order_by('-id')[0:4]
    Latest_Post = Post.objects.filter(
        section='Latest_Post', status=1).order_by('-id')[0:4]
    Main_post = Post.objects.filter(Main_post=True)[0:1]
    category = Category.objects.all()

    context = {
        'popular_post': popular_post,
        'Main_post': Main_post,

        'recent_post': recent_post,
        'Editors_Pick': Editors_Pick,
        'Trending': Trending,
        'Inspiration': Inspiration,
        'Latest_Post': Latest_Post,
        'category': category,
    }


    return render(request, 'index.html', context)


def base(request):
    return render(request, 'base.html')
