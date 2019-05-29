from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
import random
from .forms import ContactUsForm
from .models import ContactUs
  
def get_last_most_active_user(number=15):
    return random.random()*10


class HomeView(TemplateView):
    template_name='base.html'

class AboutView(FormView):
    template_name = 'pages/about.html'
    form_class = ContactUsForm
    
  

    extra_context = {'about_me':get_last_most_active_user()}
    success_url = '/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
   

    