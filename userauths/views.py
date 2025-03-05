from django.shortcuts import render
from userauths.models import User
from userauths.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, login as auth_login
from django.shortcuts import redirect
from django.conf import settings


user = settings.AUTH_USER_MODEL
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)  # Save user but don't commit yet
            new_user.set_password(form.cleaned_data["password1"])  # Hash password
            new_user.save()  # Now save the user

            messages.success(request, f'Account created for {new_user.username}!')

            # Authenticate the user
            new_user = authenticate(username=new_user.username, password=form.cleaned_data["password1"])
            if new_user is not None:
                login(request, new_user)  # Log in the user
                return redirect("core:project")  # Redirect after signup
            else:
                messages.error(request, "Authentication failed. Please log in manually.")
                return redirect("userauths:signin")

        else:
            print("Form is not valid:", form.errors)  # Debugging
    else:
        form = UserRegistrationForm()
        
    return render(request, 'userauths/signup.html', {"form": form})
   
    
def user_login(request):
    if request.user.is_authenticated:
        messages.warning(request, f'Hey, You are already logged in!')
        return redirect("core:project")

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = None  # Ensure user is defined before authentication

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, f'Account with {email} does not exist!')
        
        if user:
            user = authenticate(request, email=email, password=password)
            if user:
                auth_login(request, user)
                messages.success(request, f'Dear {user.username}, You are now logged in!')
                return redirect("core:project")
            else:
                messages.warning(request, f'Incorrect password for {email}!')

    form = UserRegistrationForm()
    return render(request, 'userauths/signin.html', {"form": form})

def user_logout(request):
    logout(request)
    messages.success(request, f'You are now logged out!')

    return redirect("userauths:signin")   