from ..accountapp.models import MyUser,BaseModel
from django.db import models
# Create your models here.

class LetterInstruction(BaseModel):       # Ko'rstma hati
   letter_name=models.CharField(max_length=50)
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   litter_number=models.CharField(unique=True,max_length=15)
   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   company_name=models.CharField(max_length=150)
   stir_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   report_name=models.CharField(max_length=100)      # hisobat nomi
   report_date=models.DateTimeField()     

   def __repr__(self) -> str:
          return f'{self.letter_name} : {self.user}'




class LetterSummons(BaseModel):       # Chaqiruv hati
   letter_name=models.CharField(max_length=50)
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   litter_number=models.CharField(unique=True,max_length=15)
   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   company_name=models.CharField(max_length=150)
   stir_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   report_name=models.CharField(max_length=100)      # hisobat nomi: 1-xatdan torib oaldi
   report_date=models.DateTimeField()    #   hisobat date: hisobat nomidan oladi


   def __repr__(self) -> str:
          return f'{self.letter_name} : {self.user}'


class LetterCourt(BaseModel):       # Sud hati
   letter_name=models.CharField(max_length=50)
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   litter_number=models.CharField(unique=True,max_length=15)
   company_name=models.CharField(max_length=150)
   ptsh=models.CharField(max_length=15)
   stir_number=models.PositiveBigIntegerField(default=0,null=True,blank=True)
   report_name=models.CharField(max_length=100)      # hisobat nomi: 2- xatdan tortib oladi
   report_date=models.DateTimeField() 
   company_own=models.CharField(max_length=50)                  

   def __repr__(self) -> str:
          return f'{self.letter_name} : {self.user}'
   



