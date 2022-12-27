from django.shortcuts import render, get_object_or_404
from .models import Product

from accounts.models import Creator
from django.contrib.auth import get_user_model


def creator_product_list(request, creator_id):
    creator = Creator.objects.get(id=creator_id)
    products = Product.objects.filter(creator=creator)

    return render(request, 'shop/product/list.html', locals())


def product_detail(request, id, slug, creator_id):
    creator = Creator.objects.get(id=creator_id)
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = 'pass'
    
    return render(request, 'shop/product/detail.html', locals())
