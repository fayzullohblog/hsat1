from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from .userchoice import MyUserChoice
# Create your models here.





class MyUser(AbstractUser):
    phone_number=models.CharField(max_length=30)
    user_number_litter=models.CharField(max_length=40,unique=True,blank=True,null=True)
    role_user=models.CharField(max_length=5,default=MyUserChoice.STAFF,choices=MyUserChoice.choices)
    state=models.BooleanField(default=False)

    EMAIL_FIELD = "phone_number"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self) -> str:
        return self.first_name


class BaseMOdel(models.Model):
    create_date=models.DateTimeField(default=timezone.now,editable=False)  #+ 30, shanbni , yakshanbi  bulsa, dushanbiga utish kerak   
    update_date=models.DateTimeField(default=timezone.now)


    class Meta:
        abstract=True

    def save(self,*args,**kwargs):
        self.update_date=timezone.now()
        super().save(*args,**kwargs)

