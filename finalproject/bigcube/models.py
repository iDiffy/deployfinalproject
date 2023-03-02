from django.db import models

# Create your models here.

class Customer(models.Model):
    cusphone = models.CharField(max_length=10, primary_key=True)
    cusname = models.TextField()
    cusemail = models.CharField(max_length=20)
    customerpassword = models.CharField(max_length=60, default="NULL")

class Menu(models.Model):
    menucode = models.CharField(max_length=2, primary_key=True)
    menuname = models.TextField()
    menuprice = models.CharField(max_length=2)

class Seller(models.Model):
    sellerid = models.CharField(max_length=10, primary_key=True)
    sellername = models.TextField()
    
class Orderlist(models.Model):
    cusphone = models.ForeignKey(Customer, on_delete=models.CASCADE)
    menucode = models.ForeignKey(Menu, on_delete=models.CASCADE)
    sellerid = models.ForeignKey(Seller, on_delete=models.CASCADE)
    orderdate = models.DateField()
    pickupdate = models.DateField()
