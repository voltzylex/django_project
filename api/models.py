
from django.db import models
from django.forms import CharField


# Create your models here.

# Creating Company model
class Company(models.Model):
               company_id = models.AutoField(primary_key = True)
               name = models.CharField( max_length=50)
               location = models.CharField(max_length = 50)
               about = models.TextField()
               type = models.CharField(max_length = 100,choices = (("IT","it"),("Non it ","non it"),("Other","other"),))
               added_data = models.BooleanField(default=True)
               active = models.DateField(auto_now=True)


  # Creating Emplloyee model
               # if you give space this shit will give error 
class Employee(models.Model):
               name = models.CharField(max_length = 50) 
               email = models.CharField(max_length = 100) 
               address = models.CharField(max_length = 200) 
               phone = models.CharField(max_length = 50) 
               name = models.CharField(max_length = 50) 
               about = models.TextField()
               positon = models.CharField(max_length = 50,choices = (("Manager","manager"),
                                                                             ("Software Developer","sd")
                                                                             ,("Project Leader","pl")
                                                                             ))
               company = models.ForeignKey(Company,on_delete = models.CASCADE)                            