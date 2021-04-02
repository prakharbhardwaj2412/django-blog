from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
posts = [
    {
    'author': 'Prakhar',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 30, 2018'
    },
    {
    'author': 'Shreya',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'March 31, 2018'
    }
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 