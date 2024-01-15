from django.db import models

# Create your models here.

# Creating Company model
class Company(models.Model):
               company_id = models.AutoField(primary_key = True)
               name = models.CharField( max_length=50)
               location = models.CharField(max_length = 50)
               about = models.TextField()
               type = models.CharField(max_length = 100,choice = (("IT","it"),("Non it ","non it"),("Other","other"),))
               added_data = models.BooleanField(default=True)
               added_dateTime = models.DateField(auto_now=True)