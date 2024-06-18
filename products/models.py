from itertools import product

from django.db import models
from customers.models import Customers
from .safe import SaveMediaFile, PriceType
from django.contrib.auth.models import User



class Comment(models.Model):
    text = models.TextField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]


class Category(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Product(models.Model):
    title = models.CharField(verbose_name='Product Name',max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=SaveMediaFile.product_image_path)
    product_price = models.CharField(max_length=50, verbose_name="Product Price", blank=True, null=True)
    price_type = models.CharField(max_length=10, choices=PriceType.choices, default=PriceType.USD)
    comments = models.ManyToManyField(Comment, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    category_code = models.CharField(max_length=50, verbose_name="Category", blank=True, null=True)
    category_name = models.CharField(max_length=50, verbose_name="Category", blank=True, null=True)
    sub_category_code = models.CharField(max_length=50, verbose_name="Sub Category", blank=True, null=True)
    sub_category_name = models.CharField(max_length=50, verbose_name="Sub Category", blank=True, null=True)


def __str__(self):
        return self.title



class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_number = models.IntegerField(default=1)
    rating = models.FloatField(default=0)
    shipping_price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def __str__(self):
        return self.product_number


class Users(models.Model):
    full_name = models.CharField(verbose_name="fullname",max_length=100,null=True,blank=False)
    username = models.CharField(verbose_name="username",max_length=100,unique=True,blank=True)
    telegram_id = models.PositiveIntegerField(verbose_name="telegram id",unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
