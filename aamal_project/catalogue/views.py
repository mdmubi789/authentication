from django.http import HttpResponse
from django.shortcuts import render
from . models import Category,Product

# Create your views here.
def catalogue(request):
    return render( request,'catalogue.html')


# Create your views here.

def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, "products.html", context)