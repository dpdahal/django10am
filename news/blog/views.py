from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    data = {
        'title': 'Welcome',
        'users': [
            {'name': 'ram', 'address': 'kathmandu'},
            {'name': 'sita', 'address': 'pokhara'},
            {'name': 'gita', 'address': 'kathmandu'},
        ]
    }
    return render(request, 'index.html', data)


def about(request):
    data = {
        'title': 'about-us'
    }
    return render(request, 'about.html', data)


def contact(request):
    return render(request, 'contact.html')


def education(request, criteria):
    return HttpResponse(criteria)


def users(request):
    return HttpResponse("all users here")


def user_detail(request, id):
    return HttpResponse("get by criteria: ")
