# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
# def detail(request, my_args):
#     Article.objects.create(title='hello,world', category='python', content='let us add database item')
#     Article.objects.create(title='django blog study', category='python', content='django blog tutorial')
#     post = Article.objects.all()[int(my_args)]
#     str = ("title= %s,category = %s,date_time = %s,content = %s"
#            % (post.title, post.category, post.date_time, post.content))
#     return HttpResponse(str)


def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
