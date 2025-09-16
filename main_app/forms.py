from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name','brand','description','category','quantity','image', 'suppliers', 'date_added'] 
    widgets = {
      'date_added': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={
          'placeholder': 'Select a date',
          'type': 'date'
        }
      ),
    }