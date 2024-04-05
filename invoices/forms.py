from django import forms
from .models import Invoice, Customer ,Product ,InvoiceItem


class InvoiceForm(forms.ModelForm):
    # Define a ModelChoiceField for customer_name
    customer_name = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label=None)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'customer_name', 'total_amount']


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['description', 'quantity', 'unit_price']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'phone_number', 'address', 'national_id', 'economic_code', 'postal_code', 'store_name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price' ,'product_number' , 'calculation_type']
