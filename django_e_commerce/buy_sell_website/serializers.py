# buy_sell_website/serializers.py

from rest_framework import serializers
from .models import Categories, Subcategories, Products

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Subcategories
        fields = ['subcategoryid', 'subcategoryname', 'categoryid']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['categoryid', 'categoryname']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  

    class Meta:
        model = Products
        fields = ['ad_no', 'description', 'price', 'city', 'image', 'category', 'subcategoryid', 'productname']
        
        
        
