from django.db import models

# Create your models here.
class tbl_register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    pswd = models.CharField(max_length=100)
    place = models.CharField(max_length=100)  
    address = models.TextField(max_length=255) 
    phone = models.CharField(max_length=100)
    utype = models.CharField(max_length=100, default="user")
    
    def __str__(self):
        return self.name


from django.db import models
from driverapp.models import DriverRegister

class ComplaintRegister(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey('tbl_register', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    ward = models.CharField(max_length=100, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', blank=True, null=True)
    bin = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    place = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    driver = models.ForeignKey('driverapp.DriverRegister', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Complaint by {self.name} - {self.status}"
