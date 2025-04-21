from django.db import models
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujrat', 'Gujrat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhan', 'Jharkhan'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Maharashtra', 'Maharashtra'),
    ('Madhaya Pradesh', 'Madhaya Pradesh'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Tripura', 'Tripura'),
    ('Telangana', 'Telangana'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman & Nicobar (UT)', 'Andaman & Nicobar (UT)'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra & Nagar Haveli and Daman & Diu (UT)', 'Dadra & Nagar Haveli and Daman & Diu (UT)'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)



class Customer(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices=STATE_CHOICES)

CATEGORY_CHOICE = (
    ('C','Camera'),
    ('M','Mens'),
    ('W','Women'),
    ('S','Sunglasses'),
    ('Sh','Shoes')
)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICE)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return str (self.id)
    
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str (self.customer)


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Canceled','Canceled')
)


class OrederPlace(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20,
    choices=STATUS_CHOICES, default='Pending')



    
