from django.shortcuts import render,redirect
from . import forms as delivery_forms
from . import models as delivery_models


def delivery_home(request):
    states = delivery_models.State.objects.all()
    districts = delivery_models.District.objects.all()
    return render(request, 'delivery/delivery_home.html', {'states': states, 'districts': districts})


def delivery_state(request):
    if request.method == 'GET':
        state_name = request.GET.get('state_name')
        print(state_name)
    states = delivery_models.State.objects.filter(state_name=state_name)
    districts = delivery_models.District.objects.filter(state=states.first().id)
    print(states,"*"*10,districts)
    return render(request, 'delivery/delivery_state.html', {'districts': districts})
# def customer_home(request):
#     states = customer_models.State.objects.all()
#     distrcts = customer_models.District.objects.all()
#     context = {
#         'states': states,
#         'districts':distrcts
#     }
#     return render(request, 'customer/home.html',
#                   context)
#
# def customer_state(request):
#     if request.method=='GET':
#         state_name=request.GET['state_name']
#         print(state_name)
#
#     states = customer_models.State.objects.filter(state_name=state_name)
#     # distrcts = customer_models.District.objects.all()
#     distrcts = customer_models.District.objects.filter(state=states.first().id)
#     context = {
#         'districts':distrcts
#     }
#     return render(request,
#                   'customer/customer_state.html',
#                   context)
def add_delivery_address(request):
    form=delivery_forms.Delivery_Form()
    return render(request, 'delivery/delivery_address.html',{'form':form})
# def add_delivery_address(request):
#     if request.method=='POST':
#         if request.POST['firstname'] and request.POST['lastname'] and request.POST['email'] and request.POST['address1'] and request.POST['address2'] and request.POST['district'] and request.POST['state'] and request.POST['pincode']:
#
#             delivery=delivery_models.Delivery_address()
#             delivery.firstname=request.POST['firstname']
#             delivery.lastname=request.POST['lastname']
#             delivery.username=request.POST['username']
#             delivery.email=request.POST['email']
#             delivery.address1=request.POST['address1']
#             delivery.address2=request.POST['address2']
#             delivery.district=request.POST['district']
#             delivery.state=request.POST['state']
#             delivery.pincode=request.POST['pincode']
#             delivery.save()
#             return redirect('restaurant_home')
#         else:
#             return render(request, 'delivery/delivery_address.html',{'error':'Please fill all fields'})
#
#     return render(request,'delivery/delivery_address.html')
#
