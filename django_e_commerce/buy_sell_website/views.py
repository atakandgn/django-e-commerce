from django.shortcuts import render, get_object_or_404
import requests
from django.http import JsonResponse
import json
from rest_framework import generics
from .serializers import CategorySerializer, ProductSerializer, SubCategorySerializer
from .models import Categories, Products, Subcategories
from django.db.models import Q,Count

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
    # Assuming 'ad_no' is the primary key field
    product = get_object_or_404(Products, ad_no=product_id)

    # Pass the product data to the template
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def search_results(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category_id', '')
    subcategory_id = request.GET.get('subcategory_id', '')

    # Initialize the base queryset
    base_queryset = Products.objects.all()

    # Filter by category if provided
    if category_id:
        base_queryset = base_queryset.filter(category_id=category_id)

    # Filter by subcategory if provided
    if subcategory_id:
        base_queryset = base_queryset.filter(subcategoryid=subcategory_id)

    # Perform a case-insensitive search on productname, description, and city
    search_results = base_queryset.filter(
        Q(productname__icontains=query) |   # Search productname containing the query
        Q(description__icontains=query) |   # Search description containing the query
        Q(city__icontains=query)            # Search city containing the query
    )

    # Pass the search results, query, and log_data to the template
    context = {'query': query, 'search_results': search_results}
    return render(request, 'search_results.html', context)


