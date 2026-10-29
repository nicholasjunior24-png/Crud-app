from.views import ProductDetailView, ProductListCreateView
from django.urls import path

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list"),
    path("products/int:pk/", ProductDetailView.as_view(), name='product-details'),
]