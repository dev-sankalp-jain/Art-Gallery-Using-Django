from django.shortcuts import render
from .models import *; 
# Create your views here.
def login():
    pass

def registration():
    pass

#  args = list , kwargs = dictionary
def home_view(request, *args, ** kwargs):
    art = Art.objects.get(id = 2)
    return render(request, "index.html", {'art':art})


def about_us():
    # about us
    pass

def cart():

    pass

def order():
    pass


# index page 
    # print(request.user)
    # if request.user != 'anonymous':
    #     # login & register page removed
    #     print(request.user)
    # else :
    #     print(request.user)
