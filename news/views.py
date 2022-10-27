from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'


class StoryDetail(DetailView):
    model = Post
    template_name = 'story.html'
    context_object_name = 'story'