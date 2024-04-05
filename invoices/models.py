# models.py
from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    total_amount = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date_created = timezone.now()
        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    national_id = models.CharField(max_length=20)
    economic_code = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    store_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_number = models.CharField(max_length=100)
    calculation_type = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
