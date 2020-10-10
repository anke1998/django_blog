from django.shortcuts import render, get_object_or_404
from .models import Blog, Tag, Category
import markdown
# Create your views here.


def index(request):
    blog_list = Blog.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'blog_list': blog_list,
    })


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.body = markdown.markdown(blog.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'blog': blog})


def archive(request, year, month):
    blog_list = Blog.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'blog_list': blog_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    blog_list = Blog.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'blog_list': blog_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    blog_list = Blog.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'blog_list': blog_list})