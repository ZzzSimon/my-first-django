from django.shortcuts import render
from django.http import HttpResponse
from blog import models


def hello(request):
    return HttpResponse('Hello,world')


def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'blog_index': blog_index,
        'url_prefix': 'detail/'
    }
    return render(request, 'index.html', context)


def detail(request, qid):
    article = models.Article.objects.get(id=qid)
    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)
