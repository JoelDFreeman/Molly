from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from erp.models import Address, Company, Contact, Product, Order

order = Order.objects.all()
company = Company.objects.all()
product = Product.objects.all()

def home(request):
    context = {
        'order':Order.objects.all()
    }
    return render(request, 'UI/home.html', {'title':'Home'})

def orders(request):
    context = {
        'order':Order.objects.all()
    }
    return render(request, 'UI/orders.html', {'title':'Orders'})

def companies(request):
    return render(request, 'UI/companies.html', {'title':'Companies'})

def products(request):
    return render(request, 'UI/products.html', {'title':'Products'})    

def test(request):
    context = {
        'order':Order.objects.all()
    }
    return render(request, 'UI/test.html', context)      

