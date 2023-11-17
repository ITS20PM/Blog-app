from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# blog post
posts = [
    {'author': 'Patrick', 
    'title': 'Blog 1',
    'content': 'First blog',
    'date': 'Jan 1st, 2023'},
    {'author': 'David', 
    'title': 'Blog 2',
    'content': 'Second blog',
    'date': 'Feb 1st, 2023'}
]


# Create your views here.
# Post.objects.all()
def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})