from django.urls import path
from .views import *
from .stock_views import *
from django.conf.urls.static import static
from django.conf import settings

#app_name = 'news'

urlpatterns = [
    #path('', welcome),
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('restricted/', restricted_view, name='restricted'),
    path('logout/', user_logout, name='logout'),
    # Add other URL patterns as needed

    # URL pattern for generating a bill
    path('bill/<int:order_id>/', generate_bill, name='generate_bill'),

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    
    # Product URLs
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Order URLs
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    # Purchase URLs
    path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('purchases/create/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchases/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchases/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase_delete'),

    # Sales URLs
    path('sales/', SalesListView.as_view(), name='sales_list'),
    path('sales/<int:pk>/', SalesDetailView.as_view(), name='sales_detail'),
    path('sales/create/', SalesCreateView.as_view(), name='sales_create'),
    path('sales/<int:pk>/update/', SalesUpdateView.as_view(), name='sales_update'),
    path('sales/<int:pk>/delete/', SalesDeleteView.as_view(), name='sales_delete'),

    # Suppliers
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
    # Add other URL patterns as needed

    #table
    path('form/', form, name='form'),
    path('icons/', icons, name='icons'),
    path('profile/', profile, name='profile'),
    path('tables/', tables, name='tables'),
    path('map/', map, name='map'),
    path('registr/', registr, name='registr'),
    path('view/', view, name='view'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
