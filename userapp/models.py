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

class ComplaintRegister(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey('tbl_register', on_delete=models.CASCADE)  # Link complaints to users
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    ward = models.CharField(max_length=100)
    location = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', blank=True, null=True)
    bin = models.BooleanField(default=False)  # True if bin is requested, False otherwise
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.name} - {self.status}"
