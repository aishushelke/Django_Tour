from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class user(AbstractUser):

    fname=models.TextField(max_length=30,null=True, blank=False)
    lname=models.TextField(max_length=30,null=True,blank=False)
    email=models.EmailField('email_address',unique=True)
    contact=models.TextField(max_length=10, null=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email