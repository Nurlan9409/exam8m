from django.shortcuts import render
from django.views import View
from .models import Product, Category, Comment, Cart
from customers.models import Customers
from django.contrib.auth.models import User

# Create your views here.


class ProductListView(View):
    def get(self, request):
        search = request.GET.get('search')
        print(search)
        if not search:
            products = Product.objects.all()
            categories = Category.objects.all()
            featured_products = Product.objects.all()
            context = {'products': products,
                       "categories": categories,
                       "featured_products": featured_products,
                       }
            return render(request, 'main/shop.html', context)
        else:
            products = Product.objects.filter(title__icontains=search)
            featured_products = Product.objects.all()
            categories = Category.objects.all()
            context = {'products': products,
                       "categories": categories,
                       "featured_products": featured_products,
                       }
            return render(request, 'main/shop.html', context)


class ProductDetailView(View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        featured_products = Product.objects.all()
        categories = Category.objects.all()
        customers = Customers.objects.all()
        comments = Comment.objects.all()
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        print(user)
        context = {
            'products': products,
            "categories": categories,
            'featured_products': featured_products,
            'customers': customers,
            'comments': comments,
            'user': user,
        }
        return render(request, 'main/shop-detail.html', context)

    def post(self, request, id):
        user = request.user
        text = request.POST.get('comment')
        comment = Comment.objects.create(text=text, user=user)
        product = Product.objects.get(id=id)
        product.comments.add(comment)
        product.save()
        featured_products = Product.objects.all()
        categories = Category.objects.all()
        customers = Customers.objects.all()
        comments = Comment.objects.all()
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        context = {
            'product': product,
            "categories": categories,
            'featured_products': featured_products,
            'customers': customers,
            'comments': comments,
            'user': user,
            }
        return render(request, 'main/shop-detail.html', context)


class CartView(View):
    def get(self, request):
        cart_items = Cart.objects.all()

        total_price = 0
        shipping_price = 0

        for cart_product in cart_items:
            total_price += cart_product.product.price
            shipping_price += cart_product.shipping_price

        context = {
            'cart': cart_items,
            'total_price_ship': total_price + shipping_price,
            'total_price': total_price,
            'shipping_price': shipping_price,
        }
        return render(request, 'main/cart.html', context)
