from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Baidurik Media',
        'title': 'My wishes',
        'content': 'I want to get my ass fucked hardly',
        'date_posted': 'April 15, 2017'
    },
    {
        'author': 'Semyon Sychev',
        'title': 'Hate you people',
        'content': 'You all are gays',
        'date_posted': 'May 5, 2018'
    }
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})