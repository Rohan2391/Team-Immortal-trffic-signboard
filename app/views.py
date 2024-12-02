from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserRegistration

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        error_message = None

        # Check if passwords match
        if password != confirm_password:
            error_message = "Passwords do not match."

        # Check if username already exists
        elif UserRegistration.objects.filter(username=username).exists():
            error_message = "Username already exists."

        # Check if email already exists
        elif UserRegistration.objects.filter(email=email).exists():
            error_message = "This email is already registered. Please use another email."

        # If there's an error, render the form with the error message
        if error_message:
            return render(request, "register.html", {"error_message": error_message})

        # Save user if no errors
        user = UserRegistration(email=email, username=username, password=password)
        user.save()

        # Redirect to login with success message
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = UserRegistration.objects.get(username=username, password=password)
            request.session["username"] = user.username
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("home")
        except UserRegistration.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")

    return render(request, "login.html")
def reset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "reset_password.html")

        try:
            user = UserRegistration.objects.get(email=email)
            user.password = new_password
            user.confirm_password = new_password
            user.save()
            messages.success(request, "Password reset successful! Please log in.")
            return redirect("login")
        except UserRegistration.DoesNotExist:
            messages.error(request, "Email not found.")
            return render(request, "reset_password.html")

    return render(request, "reset_password.html")


def home(request):
    return render(request, "home.html")