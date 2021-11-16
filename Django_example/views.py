from django.shortcuts import render, redirect

def index (request):
    return render(request, 'HTML/registration.html', context=None)
