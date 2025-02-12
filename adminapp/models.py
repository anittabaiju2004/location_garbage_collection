from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    pswd = models.CharField(max_length=100)

    def __str__(self):
        return self.email
