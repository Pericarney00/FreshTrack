from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


CATEGORIES = (
  ('D', "Dairy"),
  ('F', 'Frozen'),
  ('R', 'Refrigerated'),
  ('M&S', 'Meat & Seafood'),
  ('P/DG', 'Pantry/Dry Goods'),
  ('H', 'Houshold Items'),
  ('P', 'Produce')
)


class Supplier(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=50) 
  email = models.EmailField(blank=True, null=False)
  address = models.CharField(max_length=80)
  notes = models.TextField(blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("product-index")
  
  class Meta:
    ordering = ['name']
  


class Product(models.Model):
  name = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  description = models.TextField()
  quantity = models.IntegerField()
  category = models.CharField(
    max_length= 4,
    choices = CATEGORIES,
    default = CATEGORIES[0][0]
  )
  date_added = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  suppliers = models.ManyToManyField(Supplier, null=True)
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('product-update', kwargs={"pk": self.id})
  
  class Meta:
    ordering = ['name']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=200, blank=True)  # For accessibility
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"