from django.urls import path
from . import views
from .models import Product
# Create your views here.
urlpatterns = [
    path('',views.products,name='products'),
    path('product',views.products,name='product')
]