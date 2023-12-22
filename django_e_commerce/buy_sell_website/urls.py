# buySell/urls.py
from django.urls import path
from .views import home, product_detail, search_results
from .views import CategoryListCreateView, ProductListCreateView, SubCategoryListCreateView

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('search_results/', search_results, name='search_results'),
    
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    
    
]