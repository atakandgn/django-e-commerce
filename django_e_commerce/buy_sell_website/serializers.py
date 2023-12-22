# serializers.py

from rest_framework import serializers
from .models import Categories, Subcategories, Products

class SubCategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Subcategories
        fields = ['subcategoryid', 'subcategoryname', 'categoryid', 'product_count']

    def get_product_count(self, obj):
        return Products.objects.filter(subcategoryid=obj.subcategoryid).count()

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields = ['categoryid', 'categoryname', 'product_count']

    def get_product_count(self, obj):
        return Products.objects.filter(category_id=obj.categoryid).count()

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Products
        fields = ['ad_no', 'description', 'price', 'city', 'image', 'category', 'subcategoryid', 'productname']
