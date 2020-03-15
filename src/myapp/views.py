from django.http import Http404
from django.shortcuts import get_list_or_404, redirect, render
from .models import * 
from django.contrib.auth.models import User, auth
from datetime import datetime

#  args = list , kwargs = dictionary
def home_view(request, *args, ** kwargs):
    arts = Art.objects.all()
    return render(request, "index.html", {'arts': arts})

def description_view(request, id , *args, **kwargs):
    object = Art.objects.get(id=id)
    context = {
        'object' : object
    }
    print(object)
    return render (request, 'description.html', context)

def add(request,id, *args, **kwargs):
    # print(request.path())
    print(request.user)
    if (not request.user.is_authenticated):
        print("Warining you need to login firdt ")
        return redirect('../../../login/login')
    user_obj = User.objects.filter(username = request.user)
    art_obj = Art.objects.filter(id = id)
    obj=MyCart.objects.create(user = user_obj[0],art_id=art_obj[0], added_date = datetime.now())
    obj.save()
    return redirect('../../../')

def about_us_view(request, *args, **kwargs):
    # about us
    return render(request,"aboutus.html",{})

def cart_view(request, *args, **kwargs):

    return render(request,"cart.html",{})

def order_view(request, *args, **kwargs):
    
    return render(request,"order.html")


# index page 
    # print(request.user)
    # if request.user != 'anonymous':
    #     # login & register page removed
    #     print(request.user)
    # else :
    #     print(request.user)
