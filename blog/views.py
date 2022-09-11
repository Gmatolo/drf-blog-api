# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     return render("Welcome to the homepage")
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
