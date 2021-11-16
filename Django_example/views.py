from django.shortcuts import render, redirect

def index (request):
    return render(request, 'Django_example/HTML/registration.html', context=None)
