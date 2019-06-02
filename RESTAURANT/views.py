from django.shortcuts import (render,
                              redirect)
from . import models as rest_models
from . import forms as rest_form
from django.contrib.auth.decorators import login_required
from carts.forms import CartAddProductForm


def restaurant_home(request):
    context = {
        'restaurant': rest_models.Add_Restaurant.objects.all(),
    }
    return render(request,'restaurant/restaurant.html',context)


@login_required(login_url='login')
def add_restaurant(request):
    form=rest_form.Restaurant_Form()
    if request.method=='POST':
        form=rest_form.Restaurant_Form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant_home')
    return render(request,'restaurant/add_restaurant.html',{'form':form})


def restaurant_details(request,rest_id):
    restid=rest_models.Add_Restaurant.objects.get(id=rest_id)
    context={
        'restid': restid,
        'food_details': rest_models.FoodDetails.objects.filter(rest=rest_id),
    }
    return render(request,'restaurant/restaurant_details.html',context)


def food_details(request,rest_id,food_id):
    context={
        "food":rest_models.FoodDetails.objects.get(id=food_id),
    "rest":rest_models.Add_Restaurant.objects.get(id=rest_id),
    "recommends":rest_models.FoodDetails.objects.all()[0:6],
    "cartaddproductform":CartAddProductForm,
    }
    return render(request, 'food/food_details.html',context)


def add_food(request):
    food_form=rest_form.Food_Details_Form()
    if request.method=='POST':
        food_form=rest_form.Food_Details_Form(data=request.POST,files=request.FILES)
        if food_form.is_valid:
            food_form.save()
            return redirect('restaurant_home')
    return render(request, 'food/add_food.html', {'food': food_form})

