from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('categories/', views.categories),
    path('categories/<int:category_id>/', views.products),
    path('categories/<int:category_id>/product/<int:product_id>/', views.product),
]

urlpatterns += [
    path('api/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/products/', views.ProductListCreateAPIView.as_view()),
    path('api/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('api/product_images/', views.ProductIMGListCreateAPIView.as_view()),
    path('api/product_images/<int:pk>/', views.ProductIMGRetrieveUpdateDestroyAPIView.as_view()),
]
