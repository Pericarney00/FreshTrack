from django.urls import path 
from . import views



urlpatterns = [
  path('', views.Home.as_view(), name = 'home'),
  path('about/', views.About.as_view(), name='about'),
  path('products/', views.ProductList.as_view(), name='product-index'),
  path('products/create/', views.ProductCreate.as_view(), name='product-create'),
  path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
  path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),

  path('accounts/signup', views.signup, name='signup'),

  path('suppliers/create/', views.SupplierCreate.as_view(), name='supplier-create'),
  path('suppliers/', views.SupplierList.as_view(), name='supplier-index'),
  path('suppliers/<int:pk>/update/', views.SupplierUpdate.as_view(), name='supplier-update'),
  path('suppliers/<int:pk>/delete/', views.SupplierDelete.as_view(), name='supplier-delete'),
  path('products/<int:product_id>/add_photo/', views.add_photo, name='add_photo'),
]



