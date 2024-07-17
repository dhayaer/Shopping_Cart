from django.shortcuts import render, get_object_or_404
from .models import Product, Cart, Offer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal


def product_list(request):
    products = Product.objects.all()
    for product in products:
        if product.discount > 0:
            product.discounted_price = product.price * (Decimal('1.0') - product.discount / Decimal('100.0'))
        else:
            product.discounted_price = product.price
    return render(request, 'shop/product_list.html', {'products': products})

@csrf_exempt
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = Cart.objects.get_or_create(product=product, quantity=quantity, saved_for_later=False)
        return JsonResponse({'message': 'Product added to cart!'})

@csrf_exempt
def save_for_later(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart_item, created = Cart.objects.get_or_create(product=product, saved_for_later=True)
        return JsonResponse({'message': 'Product saved for later!'})

def offers_list(request):
    offers = Offer.objects.all()
    return render(request, 'shop/offers_list.html', {'offers': offers})
