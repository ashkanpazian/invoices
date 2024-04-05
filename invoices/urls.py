from django.urls import path
from . import views
from .views import invoice_list,add_invoice,invoice_detail,add_customer,customer_list,add_product,product_list


urlpatterns = [
    path('', invoice_list, name='invoice_list'),
    path('add/', add_invoice, name='add_invoice'),
    path('<int:invoice_id>/', invoice_detail, name='invoice_detail'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customers/', customer_list, name='customer_list'),
    path('invoices/add_product/', views.add_product, name='add_product'),
    path('products/', product_list, name='product_list'),

]