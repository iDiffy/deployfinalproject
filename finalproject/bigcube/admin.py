from django.contrib import admin
from .models import Customer,Menu,Seller,Orderlist

# Register your models here.
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Seller)
admin.site.register(Orderlist)