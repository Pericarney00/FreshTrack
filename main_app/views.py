from django import forms
from django.shortcuts import render
from .models import Product, Supplier
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from .forms import ProductForm



# Create your views here.


class Home(LoginView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

class ProductList(ListView):
  model = Product
  
class ProductCreate(CreateView):
  model= Product
  form_class = ProductForm

  success_url = '/products/'
  
  def form_valid(self, form):
      form.instance.user =self.request.user
      return super().form_valid(form)
  
class ProductUpdate(UpdateView):
  model = Product
  form_class = ProductForm

  success_url = '/products/'

class ProductDelete(DeleteView):
  model = Product
  success_url = '/products/'