from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Марка авто')

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марки авто'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Марка авто")
    name = models.CharField(max_length=128, verbose_name="Модель")
    price = models.PositiveBigIntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name


class ProductImg(models.Model):
    image = models.ImageField(upload_to="static/img", verbose_name="Изображение автомобиля")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Модель")

    class Meta:
        verbose_name = 'Изображение автомобиля'
        verbose_name_plural = 'Изображение автомобилей'

    def __str__(self):
        return f'Изображение автомобиля - {self.product}'
