from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import os

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='category', blank=True)

    def __str__(self):
        return self.name


class Manufactorer(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.SET_NULL)
    manufactorer = models.ForeignKey(
        'Manufactorer', null=True, blank=False,
        on_delete=models.SET_NULL,
        help_text='if missing, you can add the manufactorer on the dedicated form on this page')
    name = models.CharField(max_length=254,)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='media/', blank=False,
    #                           null=False,
    #                           default='mobile-2468068_1920.png')
    image = models.ImageField (blank=False, null=False, default='mobile-2468068_1920.jpg')                          
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    latest = models.BooleanField(default=False)
    best = models.BooleanField(default=False)

    def get_url(self):
        return reverse('product_detail', args=[self.id])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class CaroPics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    image = models.ImageField(blank=False)

    class Meta:
        verbose_name_plural = 'Caro Pics'

    # def __str__(self):
    #     return self.image

    def filename(self):
        return os.path.basename(self.image.name)
