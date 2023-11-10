from django.db import models

# Create your models here.

class Query(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    Service = models.TextField()
    date = models.DateField(auto_now_add=True)

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    transactionid = models.EmailField()
    price = models.TextField()
    Service = models.TextField()
    date = models.DateField(auto_now_add=True)
    
