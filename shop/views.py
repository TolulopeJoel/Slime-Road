from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from accounts.models import Creator
from orders.forms import OrderCreateForm

from .models import Product


def creator_product_list(request, creator_id):
    creator = Creator.objects.get(id=creator_id)
    products = Product.objects.filter(creator=creator)

    return render(request, 'shop/product/list.html', locals())


def product_detail(request, id, slug, creator_id):
    creator = Creator.objects.get(id=creator_id)
    product = get_object_or_404(Product, id=id, slug=slug)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST) 

        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.paid = False

            payment_price = order.price
            product_price = product.price

            if product_price == 0.00:
                    form.save()
                    messages.success(request, f'${payment_price} payment accepted')
                    # return redirect(reverse('payment:process'))
            elif payment_price >= product_price:
                    form.save()
                    messages.success(request, f'${payment_price} payment accepted')
                    # return redirect(reverse('payment:process'))
            else:
                messages.error(request, f'${payment_price} lower than product\'s price ${product_price}')
    else:
        form = OrderCreateForm()

    return render(request, 'shop/product/detail.html', locals())
