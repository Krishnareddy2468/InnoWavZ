from django.shortcuts import render 

def index(request):
    return render(request, 'InnoWavZ/templates/core/index.html')  # Corrected path
def project(request):
    return render(request, 'InnoWavZ/templates/core/project.html')  # Corrected path
def about(request):
    return render(request, 'InnoWavZ/templates/core/about.html')  # Corrected
def contact(request):
    return render(request, 'InnoWavZ/templates/core/contact.html')  # Corrected
def services(request):
    return render(request, 'InnoWavZ/templates/core/service.html')  # Corrected