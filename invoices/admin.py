from django.contrib import admin
from .models import Invoice,InvoiceItem,Product,Customer

# Register your models here.

admin.site.register(Invoice),
admin.site.register(InvoiceItem)
admin.site.register(Product)
admin.site.register(Customer)