from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView  

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer, Product, Order, Purchase, Sales, OrderItem, Supplier  
from .forms import CustomerForm, ProductForm, OrderForm, PurchaseForm, SalesForm


# store management system
    
# Customer views
class CustomerListView(ListView):
    model = Customer
    template_name = 'store/list/customer_list.html'  # Create this template

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'store/details/customer_detail.html'  # Create this template

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'store/forms/customer_form.html'  # Create this template
    success_url = '/customers/'  # Adjust the URL as needed

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'store/forms/customer_form.html'  # Create this template
    success_url = '/customers/'  # Adjust the URL as needed

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'store/customer_confirm_delete.html'  # Create this template
    success_url = '/customers/'  # Adjust the URL as needed

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'store/list/product_list.html'
    context_object_name = 'product_list'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/details/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'store/forms/product_form.html'
    success_url = '/products/'
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/forms/product_form.html'
    success_url = '/products/'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'
    template_name = 'store/product_confirm_delete.html'

# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'store/list/order_list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'store/details/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'store/forms/order_form.html'
    success_url = '/orders/'

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'store/forms/order_form.html'
    success_url = '/orders/'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/orders/'
    template_name = 'store/order_confirm_delete.html'


# Purchase Views
class PurchaseListView(ListView):
    model = Purchase
    template_name = 'store/list/purchase_list.html'

class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'store/details/purchase_detail.html'

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'store/forms/purchase_form.html'
    success_url = '/purchases/'

class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'store/forms/purchase_form.html'
    success_url = '/purchases/'

class PurchaseDeleteView(DeleteView):
    model = Purchase
    success_url = '/purchases/'
    template_name = 'store/purchase_confirm_delete.html'


# Sales Views
class SalesListView(ListView):
    model = Sales
    template_name = 'store/list/sales_list.html'

class SalesDetailView(DetailView):
    model = Sales
    template_name = 'store/details/sales_detail.html'

class SalesCreateView(CreateView):
    model = Sales
    form_class = SalesForm
    template_name = 'store/forms/sales_form.html'
    success_url = '/sales/'

class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'store/forms/sales_form.html'
    success_url = '/sales/'

class SalesDeleteView(DeleteView):
    model = Sales
    success_url = '/sales/'
    template_name = 'store/sales_confirm_delete.html'


# Supplier

class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/list/supplier_list.html'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'store/details/supplier_detail.html'
class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'store/forms/supplier_form.html'
    success_url = '/suppliers/'
    fields = '__all__'

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'store/forms/supplier_form.html'
    success_url = '/suppliers/'
    fields = '__all__'

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'store/supplier_confirm_delete.html'
    success_url = '/suppliers/'  # Redirect to the supplier list page after deletion

def generate_bill(request, order_id):
    # Retrieve the order object from the database
    order = get_object_or_404(Order, id=order_id)
    
    # Assuming Order model has a many-to-many relationship with Product model through OrderItem
    order_items = order.orderitem_set.all()

    # Calculate the total amount for the order
    total_amount = sum(item.product.price * item.quantity for item in order_items)
    
    # Pass the necessary data to the bill template
    context = {
        'order': order,
        'order_items': order_items,
        'total_amount': total_amount,
    }
    
    # Render the bill template with the data
    return render(request, 'billing/bill.html', context)

'''def generate_bill(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    total_amount_with_gst = sum(item.product.total_price_with_gst * item.quantity for item in order_items)

    context = {
        'order': order,
        'order_items': order_items,
        'total_amount_with_gst': total_amount_with_gst
    }
    return render(request, 'billing/bill.html', context)'''

def form(request):
    #return render(request, 'home/form.html')
    return render(request, ['store/forms/customer_form.html'])

def icons(request):
    return render(request, 'home/icons.html')
def profile(request):
    return render(request, 'home/profile.html')
def tables(request):
    return render(request, 'home/tables.html')
def map(request):
    return render(request, 'home/map.html')
def registr(request):
    return render(request, 'home/registr.html')

def view(request):
    return render(request, ['store/list/order_list.html'])

    

'''class view():
    template_name = 'home/view.html'
    success_url = '/suppliers/'''



# Similar views for Product, Order, Purchase, and Sales
