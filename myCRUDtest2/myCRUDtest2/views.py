from django.shortcuts import render

from products.models import Products

def home(request):
    products = Products.objects.all()
    return render(request, 'home.html', {
        "products": products,
    })