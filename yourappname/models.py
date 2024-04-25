from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Specify the related names for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, verbose_name='user permissions')

    def __str__(self):
        return self.username
    
# store management system ---------------------------------------------------------------->
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    # Add any other relevant fields

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    # Add any other relevant fields

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    gst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=18)  # Default GST rate of 18%

    @property
    def gst_amount(self):
        """Calculates the GST amount based on the product price and GST rate."""
        return (self.price * self.gst_rate) / 100

    @property
    def total_price_with_gst(self):
        """Calculates the total price including GST."""
        return self.price + self.gst_amount
    # Add any other relevant fields

    def __str__(self):
        return self.name
    

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    quantity_purchased = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add any other relevant fields

class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField()
    quantity_sold = models.PositiveIntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add any other relevant fields

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[("Processing", "Processing"), ("Shipped", "Shipped"), ("Delivered", "Delivered")])
    # Add any other relevant fields

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"  

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def subtotal(self):
        """Calculate the subtotal for this order item."""
        return self.product.price * self.quantity

    def __str__(self):
        """Return a string representation of the order item."""
        return f"{self.quantity} x {self.product.name}"


class Bill(models.Model):
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add other fields as needed, such as billing address, payment status, etc.

    def __str__(self):
        return f'Bill #{self.id} - Customer: {self.customer.username}, Total Amount: {self.total_amount}'


