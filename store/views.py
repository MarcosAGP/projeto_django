from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Sale
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('home')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        if item.quantity > item.product.stock:
            messages.error(request, f"Estoque insuficiente para {item.product.name}")
            return redirect('view_cart')

    for item in cart_items:
        item.product.stock -= item.quantity
        item.product.save()

        Sale.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.total_price()
        )

    cart_items.delete()
    messages.success(request, "Compra realizada com sucesso!")
    return redirect('home')
