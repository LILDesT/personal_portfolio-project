from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    projects1 = Blog.objects.order_by('-Data')[:5]
    return render(request, 'blog/all_blogs.html', {'projects1':projects1})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})

