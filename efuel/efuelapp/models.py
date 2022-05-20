from django.db import models
from django.contrib.auth.models import User


class user_registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='user')
    def __str__(self):
        return self.fullname

class bunk(models.Model):
    owner_ide =  models.CharField(max_length=240,null=True)
    bunk_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    connector = models.CharField(max_length=100)
    email = models.EmailField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    address =models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=240, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.bunk_name

class category(models.Model):
    category_name = models.CharField(max_length=225)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='images/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.product_name

class bunk_booked(models.Model):
    Bunk = models.ForeignKey(bunk, on_delete=models.CASCADE, null=True)
    user_ide = models.IntegerField(default='0', null=True, blank=True)
    bunkowner_ide = models.CharField(max_length=240,null=True)
    name = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    uservehicle_type = models.CharField(max_length=100)
    userconnector = models.CharField(max_length=100)
    date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    time = models.TimeField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.name

class payment(models.Model):
    user_ide = models.CharField(max_length=240,null=True)                      
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    payment = models.CharField(max_length=240, null=True)
    bank = models.CharField(max_length=240, null=True)
    accountnumber = models.CharField(max_length=240, null=True)
    ifse = models.CharField(max_length=240, null=True) 

    def __str__(self):
        return self.user_ide

class owner_contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=240, null=True)
    subject = models.CharField(max_length=100)
    message =models.CharField(max_length=225)

    def __str__(self):
        return self.name

class admin_contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=240, null=True)
    subject = models.CharField(max_length=100)
    message =models.CharField(max_length=225)
    
    def __str__(self):
        return self.name


class Order(models.Model):
	customer = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    user_ide = models.CharField(max_length=240,null=True)
    name = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    items = models.CharField(max_length=240, null=True)
    price = models.CharField(max_length=240, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address