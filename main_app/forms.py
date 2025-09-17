from django import forms
from .models import Product, Supplier


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

  def __init__(self, *args, **kwargs ):
    user =kwargs.pop('user', None)
    super().__init__(*args, **kwargs)

    if user is not None:
      self.fields['suppliers'].queryset = Supplier.objects.filter(user=user)
      