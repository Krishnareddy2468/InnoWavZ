from django.shortcuts import render 

def index(request):
    return render(request, 'core/index.html')  # Corrected path
def project(request):
    return render(request, 'core/project.html')  # Corrected path
def about(request):
    return render(request, 'core/about.html')  # Corrected
def contact(request):
    return render(request, 'core/contact.html')  # Corrected
def services(request):
    return render(request, 'core/service.html')  # Corrected