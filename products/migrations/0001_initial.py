# Generated by Django 5.0.6 on 2024-06-18 14:32

import django.db.models.deletion
import products.safe
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True, verbose_name='fullname')),
                ('username', models.CharField(blank=True, max_length=100, unique=True, verbose_name='username')),
                ('telegram_id', models.PositiveIntegerField(unique=True, verbose_name='telegram id')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Product Name')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=products.safe.SaveMediaFile.product_image_path)),
                ('product_price', models.CharField(blank=True, max_length=50, null=True, verbose_name='Product Price')),
                ('price_type', models.CharField(choices=[('$', '$'), ('Som', 'SOM')], default='$', max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category')),
                ('category_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category')),
                ('sub_category_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sub Category')),
                ('sub_category_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sub Category')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('comments', models.ManyToManyField(blank=True, to='products.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.IntegerField(default=1)),
                ('rating', models.FloatField(default=0)),
                ('shipping_price', models.FloatField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
