from django.shortcuts import render
from .models import Category, Post

def frontpage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/templates/frontpage.html', context)
