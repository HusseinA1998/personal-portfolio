from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs_all = Blog.objects.order_by('-date_time')
    return render(request, 'blog/home.html', {'blogs': blogs_all})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'id': blog})
