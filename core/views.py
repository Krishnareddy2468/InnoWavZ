from django.shortcuts import render 
from .models import Category, Vendor, Product , ProductImage
def index(request):
    return render(request, 'core/index.html')  
def project(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'core/project.html',context)  
def about(request):
    return render(request, 'core/about.html')  
def contact(request):
    return render(request, 'core/contact.html') 
def services(request):
    return render(request, 'core/service.html') 

