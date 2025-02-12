from django.shortcuts import render,get_object_or_404

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



from django.shortcuts import render
from driverapp.models import DriverRegister


def admin_view_driver(request):
    pending_drivers = DriverRegister.objects.filter(status='pending')  
    return render(request, 'admin_view_driver.html', {'drivers': pending_drivers})

def approve_driver(request, driver_id):
    driver = get_object_or_404(DriverRegister, id=driver_id)
    driver.status = 'approved'
    driver.save()
    return redirect('admin_view_driver')

def reject_driver(request, driver_id):
    driver = get_object_or_404(DriverRegister, id=driver_id)
    driver.status = 'rejected'
    driver.save()
    return redirect('admin_view_driver')

def view_approved_drivers(request):
    approved_drivers = DriverRegister.objects.filter(status='approved')  
    return render(request, 'view_approved_drivers.html', {'drivers': approved_drivers})

def view_rejected_drivers(request):
    rejected_drivers = DriverRegister.objects.filter(status='rejected')  
    return render(request, 'view_rejected_drivers.html', {'drivers': rejected_drivers})



from django.shortcuts import render
from userapp.models import ComplaintRegister

def view_complaints(request):
    complaints = ComplaintRegister.objects.all().order_by('-date')  # Fetch complaints sorted by latest first
    return render(request, 'admin_view_complaints.html', {'complaints': complaints})

from driverapp.models import DriverRegister  # ✅ Correct
def assign_driver(request, complaint_id, driver_id):
    complaint = get_object_or_404(ComplaintRegister, id=complaint_id)
    driver = get_object_or_404(DriverRegister, id=driver_id)

    complaint.driver = driver  # Assign driver
    complaint.status = 'allocated'  # Update status
    complaint.save()

    return redirect('view_complaints')  # Redirect back to complaints page
from django.shortcuts import render, get_object_or_404, redirect
from userapp.models import ComplaintRegister
from driverapp.models import  DriverRegister


def allocate_complaint(request, complaint_id):
    complaint = get_object_or_404(ComplaintRegister, id=complaint_id)

    # Try to get drivers in the same place as the complaint's place
    drivers = DriverRegister.objects.filter(place=complaint.place, status='approved')

    # If no drivers are found, get all approved drivers
    if not drivers.exists():
        drivers = DriverRegister.objects.filter(status='approved')

    return render(request, 'allocate_complaint.html', {'complaint': complaint, 'drivers': drivers})
