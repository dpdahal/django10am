from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def education(request, criteria):
    return HttpResponse(criteria)


def users(request):
    return HttpResponse("all users here")


def user_detail(request, id):
    return HttpResponse("get by criteria: ")
