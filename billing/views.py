from django.shortcuts import render
from django.views.generic import View
from .models import Post


class CheckOutView(View):
    def get(self, request):
        return render(request, 'main/chackout.html')


class BlogView(View):
    def get(self, request):
        posts = Post.objects.all()  # Получаем все объекты Post из базы данных
        return render(request, 'main/blog.html', {'posts': posts})
