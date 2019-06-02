from django.shortcuts import render, redirect, get_object_or_404
# from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
# from .models import Cart
from .cart import Cart
from .forms import CartAddProductForm
from RESTAURANT.models import FoodDetails



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(FoodDetails, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(FoodDetails, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        print(item['image'])
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
        # food=FoodDetails.objects.filter(id=product_id)
    return render(request, 'carts/detail.html', {'cart': cart,})
# def view(request):
#     cart=Cart.objects.all()[0]
#     context={"cart":cart}
#     template="carts/view.html"
#     return render(request,template,context)
#
# def update_cart(request,slug):
#     cart=Cart.objects.all()[0]
#     try:
#         product=FoodDetails.objects.get(slug=slug)
#     except FoodDetails.DoesNotExist:
#         pass
#     except:
#         pass
#     if not product in cart.products.all():
#         cart.products.add(product)
#     else:
#         cart.products.remove(product)
#     return HttpResponseRedirect(reverse("cart"))
