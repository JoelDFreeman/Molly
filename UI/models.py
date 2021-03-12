from django.db import models
from erp.models import company, order, product
from erp.models import Address, Company, Contact, Product, Order

class order_table(models.Model):
     name = models.CharField(max_length=20)