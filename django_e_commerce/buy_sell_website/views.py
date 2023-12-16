from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from rest_framework import generics
from .serializers import CategorySerializer, ProductSerializer, SubCategorySerializer
from .models import Categories, Products, Subcategories


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = Subcategories.objects.all()
    serializer_class = SubCategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer






def home(request):
    # Your view logic here
    return render(request, 'home.html', {})

def product_detail(request, product_id):
    # Your view logic here
    return render(request, 'product_detail.html', {})

def search_results(request):
    # Your view logic here
    return render(request, 'search_results.html', {})
