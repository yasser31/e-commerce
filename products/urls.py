from django.urls import path
from. import views

urlpatterns = [
    path('', views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view())
]

