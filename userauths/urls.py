from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path("sign-up/", views.register, name='signup'),
    path("sign-in/", views.user_login, name='signin'),
    path("sign-out/", views.user_logout, name='signout'),
]