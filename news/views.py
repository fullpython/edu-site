from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import News

class NewsListView(ListView):
    model = News
    queryset = News.objects.filter(is_published=True).all()
    template_name = 'news/news_list.html'

class DraftsListView(LoginRequiredMixin,ListView):
    model = News
    queryset = News.objects.filter(is_published=False).all()
    template_name = 'news/news_list.html'
    

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


class NewsDeleteView(LoginRequiredMixin,DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url  = reverse_lazy('news_list')
    context_object_name = 'news'
    

class NewsCreateView(LoginRequiredMixin,CreateView):
    model = News
    fields = ['title','body','image','is_published']
    template_name = 'news/news_create.html'
    success_url = reverse_lazy('news_list')

class NewsUpdateView(LoginRequiredMixin,UpdateView):
    model  = News
    fields =  ['title','body','image','is_published']
    template_name = 'news/news_update.html'
    success_url = reverse_lazy('news_list')


