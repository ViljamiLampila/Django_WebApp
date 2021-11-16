from django.shortcuts import render, redirect

def index (request):
    return render(request, 'Django_example/html/registration.html', context=None)
