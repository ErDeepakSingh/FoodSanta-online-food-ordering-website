from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect
from RESTAURANT.models import FoodDetails

def food_santa_home(request):
    return render(request,'FOODSANTA/food_santa_home.html')

def search(request):
    try:
        q=request.GET.get("q")
    except:
        q=None
    if q:
        food=FoodDetails.objects.filter(food_title__icontains=q)
        context = {'query':q,'foods':food}
        template = "FOODSANTA/search_results.html"
    else:
        context = {}
        template = "FOODSANTA/food_santa_home.html"
    return render(request,template,context)

def about_us(request):
    return render(request,'FOODSANTA/about_us.html')