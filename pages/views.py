from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactUsForm
from .models import ContactUs

class HomeView(TemplateView):
    template_name='base.html'

class AboutView(FormView):
    template_name = 'pages/about.html'
    form_class = ContactUsForm

    success_url = '/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
   

    