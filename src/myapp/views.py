from django.shortcuts import render
from .models import *; 
# Create your views here.
def login():
    pass

def registration():
    pass

#  args = list , kwargs = dictionary
def home_view(request, *args, ** kwargs):
    arts = Art.objects.values()
    myList = []
    for art in arts:
        myList.append(Art.objects.get(id = art['id']))
    return render(request, "index.html", {'arts': myList})


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
