from django.shortcuts import render

from django.shortcuts import render, redirect

def admin_index(request):
    if not request.session.get("admin_logged_in"):
        return redirect("admin_login")  # Redirect if not logged in
    
    return render(request, "admin_index.html")

def admin_logout(request):
    request.session.flush()  # Clear session
    messages.success(request, "You have been logged out.")
    return redirect("admin_login")


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import tbl_admin  # Import the admin model

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the email and password match the admin credentials
        if email == "admin@gmail.com" and password == "admin":
            request.session["admin_logged_in"] = True  # Store login session
            messages.success(request, "Login successful!")
            return redirect("admin_index")  # Redirect to admin dashboard

        else:
            messages.error(request, "Invalid email or password. Please try again.")
    
    return render(request, "admin_login.html")  # Render login page