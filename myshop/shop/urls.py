from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('save-for-later/<int:product_id>/', views.save_for_later, name='save_for_later'),
    path('offers/', views.offers_list, name='offers_list'),
]
