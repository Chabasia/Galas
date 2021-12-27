from django.shortcuts import render
from .models import Category, Product, ProductImg
from .serializers import CategorySerializer, ProductSerializer, ProductIMGSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


def index(request):
    return render(request, "index.html")


def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {'categories': categories})


def products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, "products.html", {'category': category, "products": products})


def product(request, category_id, product_id):
    product = Product.objects.get(id=product_id)
    imgs = ProductImg.objects.filter(product=product)
    return render(request, "product.html", {"product": product, "imgs": imgs})


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductIMGListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductIMGSerializer
    queryset = ProductImg.objects.all()


class ProductIMGRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductIMGSerializer
    queryset = ProductImg.objects.all()
