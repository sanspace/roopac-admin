from django.contrib import admin

from .models import Customer, Order, Supplier, PurchaseOrder

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Supplier)
admin.site.register(PurchaseOrder)
