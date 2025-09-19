from django import forms
from .forms import ProductForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Product, Supplier
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-index')
        else: 
            error_message = 'Invalid sign up -try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

class ProductList(LoginRequiredMixin, ListView):
  model = Product


  def get_queryset(self):
    queryset = Product.objects.filter(user=self.request.user)
    return queryset
  
class ProductCreate(LoginRequiredMixin, CreateView):
  model= Product
  form_class = ProductForm

  success_url = '/products/'

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    form.instance.user =self.request.user
    return super().form_valid(form)
  
class ProductUpdate(LoginRequiredMixin, UpdateView):
  model = Product
  form_class = ProductForm
  success_url = '/products/'

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

class ProductDelete(LoginRequiredMixin, DeleteView):
  model = Product
  success_url = '/products/'

class SupplierCreate(LoginRequiredMixin, CreateView):
  model = Supplier
  fields = ['name', 'phone', 'email', 'address', 'notes']

  success_url = '/suppliers/'

  def form_valid(self, form):
    form.instance.user =self.request.user
    return super().form_valid(form)

class SupplierList(LoginRequiredMixin, ListView):
  model = Supplier
  success_url = '/suppliers/'

  def get_queryset(self):
    queryset = Supplier.objects.filter(user=self.request.user)
    return queryset
  
class SupplierUpdate(LoginRequiredMixin, UpdateView):
  model = Supplier
  fields = ['name', 'phone', 'email', 'address', 'notes']

  success_url = '/suppliers/'

class SupplierDelete(LoginRequiredMixin, DeleteView):
  model = Supplier
  success_url = '/suppliers/'


