from django.contrib import admin
from .models import Product, Offer, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Offer)
admin.site.register(Cart)

