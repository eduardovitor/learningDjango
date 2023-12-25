from django.shortcuts import render, HttpResponse

# Create your views here.
def soma(request,num1,num2):
    return HttpResponse("A soma foi {}".format(num1+num2))