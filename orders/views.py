from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import OrderItem,Order
from .forms import OrderCreateForm
from orders.paytm import Checksum
from carts.cart import Cart

MERCHANT_KEY = '7s&BTowB&lexzvOP'

def order_details(request):
    order=OrderItem.objects.all()

    return render(request,'orders/order/order_details.html',{'orders':order})

@login_required(login_url='login')
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                ammount=item['price']
            # clear the cart
            param_dict={
                'MID': 'lENwsL85644795729805',
                'ORDER_ID': str(order.id),
                'TXN_AMOUNT': str(ammount),
                'CUST_ID': order.email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/orders/handlepayment/',
            }
            param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
            cart.clear()
            return render(request, 'orders/order/paytm.html', {'param_dict': param_dict})
            # return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
@csrf_exempt
def handlepayment(request):
    form=request.POST
    response_dict={}
    for i in form.keys():
        response_dict[i]=form[i]
        if i=='CHECKSUMHASH':
            checksum=form[i]
    verify=Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print("Order Successfull")
        else:
            print("Order was not Successfull because "+response_dict['RESPMSG'])
    return render(request,'orders/order/paymentstatus.html',{'response':response_dict})
