from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

# CreateView, DetailView, UpdateView, DeleteView


# Create your views here.




class Home(LoginView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'