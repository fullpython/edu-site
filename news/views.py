from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import News

class NewsList(ListView):
    model = News
    queryset = News.objects.filter(is_published=True).all()
    template_name = 'news/news_list.html'


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
    


