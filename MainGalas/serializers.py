from rest_framework import serializers
from .models import Category, Product, ProductImg


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "category"]


class ProductIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ["image", "product"]
