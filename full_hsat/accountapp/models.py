from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    phone_number=models.CharField(max_length=30)
    user_number_litter=models.CharField(max_length=40,unique=True,blank=True,null=True)


    EMAIL_FIELD = "phone_number"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self) -> str:
        return self.first_name

