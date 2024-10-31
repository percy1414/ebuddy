from django.shortcuts import render, HttpResponse

# Create your views here.
def playtime(request):
    return render(request, 'ebuddy/cash.html')

def base(request):
    return render(request, 'ebuddy/base.html')

def homepage(request):
    return render(request, 'ebuddy/homepage.html')

def saso(request):
    return render(request, 'ebuddy/saso.html')

def tagsaso(request):
    return render(request, 'ebuddy/tagsaso.html')

def registrar(request):
    return render(request, 'ebuddy/registrar.html')

def tagregistrar(request):
    return render(request, 'ebuddy/tagregistrar.html')

def cashier(request):
    return render(request, 'ebuddy/cashier.html')

def tagcashier(request):
    return render(request, 'ebuddy/tagcashier.html')