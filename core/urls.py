from django.urls import path
from core import views
from django.urls import path
from django.urls import reverse
app_name = "core"

urlpatterns = [
    path("", views.index , name="home"),
    path("project", views.project, name="project"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("service", views.services, name="service"),
]


