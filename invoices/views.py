# views.py
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice, InvoiceItem ,Customer,Product
from .forms import InvoiceForm, InvoiceItemForm, CustomerForm,ProductForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomerForm


InvoiceItemFormSet = modelformset_factory(InvoiceItem, fields=('description', 'quantity', 'unit_price'))


def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})


def add_invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        customer_form = CustomerForm(request.POST)
        item_formset = InvoiceItemFormSet(request.POST)
        if invoice_form.is_valid() and customer_form.is_valid() and item_formset.is_valid():
            print(invoice_form)
            customer = customer_form.save()  # Save customer information
            invoice = invoice_form.save(commit=False)
            invoice.customer_name = customer.full_name  # Set customer name in invoice
            invoice.save()  # Save invoice information

            for form in item_formset:
                if form.cleaned_data:
                    item = form.save(commit=False)
                    item.invoice = invoice
                    item.save()
            return redirect('invoice_list')
    else:
        invoice_form = InvoiceForm()
        customer_form = CustomerForm()
        item_formset = InvoiceItemFormSet()
    return render(request, 'invoices/add_invoice.html', {'invoice_form': invoice_form, 'customer_form': customer_form, 'item_formset': item_formset})


def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # مثلاً به لیست فاکتورها هدایت شود
    else:
        form = CustomerForm()
    return render(request, 'invoices/add_customer.html', {'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'invoices/customer_list.html', {'customers': customers})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # یا هر صفحه دیگری که باید به آن منتقل شود
    else:
        form = ProductForm()

    return render(request, 'invoices/add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'invoices/product_list.html', {'products': products})


def get_products(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name} for product in products]
    return JsonResponse({'products': data})
