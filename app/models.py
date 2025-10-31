from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('interpreter', 'Interpreter'),
        ('staff', 'Staff'),
        ('company_admin', 'Company Admin'),
        ('super_admin', 'Super Admin'),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='client')
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
