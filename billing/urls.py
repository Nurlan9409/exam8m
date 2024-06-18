from django.urls import path
from .views import CheckOutView, BlogView

urlpatterns = [
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('blog/', BlogView.as_view(), name="blog")
]

