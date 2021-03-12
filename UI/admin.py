from django.contrib import admin
from erp.models import company, order, product
from erp.models import Address, Company, Contact, Product, Order

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Order)

# Register your models here.
