from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Products


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('Success!')
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'form.html', {'form': form})

def detail_product(request, p_id):
    p = Products.objects.get(pk = p_id)
    return render(request, 'detail-product.html', {"p": p})

def update_product(request, p_id):
    p = Products.objects.get(pk=p_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p )
        if form.is_valid():
            form.save()
            #return HttpResponse('Success!')
            return redirect('/')
    else:
        form = ProductForm(instance=p)
    return render(request, 'form.html', {'form': form})

def delete_product(request, p_id):
    Products.objects.get(pk=p_id).delete()
    #return render(request, 'home.html')
    return  redirect('/')
