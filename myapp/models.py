from django.db import models

# Create your models here.

class appointmenttable(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Date = models.DateField()
    Departement = models.CharField(max_length=50)
    Number = models.BigIntegerField()
    Message = models.TextField()

class commenttable(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Website = models.CharField(max_length=20)
    Message = models.TextField()

class contacttable(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Subject = models.TextField()
    Message = models.TextField()

class registertable(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Number = models.BigIntegerField()
    Password = models.CharField(max_length=25)
    Address = models.TextField()
    role = models.IntegerField(null=True)
