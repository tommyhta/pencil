from __future__ import unicode_literals
from django.db import models
import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validator(self,posted):
        error = {}
        if len(posted['first_name']) < 1:
            error['first_name'] = "This field cannot be empty."
        elif len(posted['first_name']) < 2:
            error['first_name'] = "Name should be longer."
        elif not str.isalpha(posted['first_name']):
            error['first_name'] = "Name cannot contain numbers."
        if len(posted['last_name']) < 1:
            error['last_name'] = "This field cannot be empty."
        elif len(posted['last_name']) < 2:
            error['last_name'] = "Name should be longer."
        elif not str.isalpha(posted['last_name']):
            error['last_name'] = "Name cannot contain numbers."
        if len(posted['email']) < 1:
            error['email'] = "This field cannot be empty."
        elif not email_regex.match(posted['email']):
            error['email'] = "Please enter a valid email."
        elif len(User.objects.filter(email=posted['email'])):
            error['email'] = "Please use a different email."
        if len(posted['password']) < 1:
            error['password'] = "This field cannot be empty."
        elif len(posted['password']) < 8:
            error['password'] = "Password must be at least 8 characters."
        elif not re.search(r'[A-Z]+', posted['password']):
            error['password'] = "Password must contain an uppercase letter."
        elif not re.search(r'[0-9]+', posted['password']):
            error['password'] = "Password must contain a number."
        if len(posted['confirm']) < 1:
            error['confirm'] = "This field cannot be empty."
        elif posted['confirm'] != posted['password']:
            error['confirm'] = "Password confirmation must match password."
        return error

    def loginValidator(self,posted):
        error = {}
        if len(posted['emaillogin']) < 1:
            error['log'] = "Please enter your email."
        if len(posted['key']) < 1:
            error['key'] = "Please enter your password."
        return error            

    def updateInfoValidator(self, posted):
        error = {}
        if len(posted['first_name']) < 1:
            error['first_name'] = "This field cannot be empty."
        elif len(posted['first_name']) < 2:
            error['first_name'] = "Name should be longer."
        elif not str.isalpha(posted['first_name']):
            error['first_name'] = "Name cannot contain numbers."
        if len(posted['last_name']) < 1:
            error['last_name'] = "This field cannot be empty."
        elif len(posted['last_name']) < 2:
            error['last_name'] = "Name should be longer."
        elif not str.isalpha(posted['last_name']):
            error['last_name'] = "Name cannot contain numbers."
        if len(posted['email']) < 1:
            error['email'] = "This field cannot be empty."
        elif not email_regex.match(posted['email']):
            error['email'] = "Please enter a valid email."
        return error

    def updatePW(self, posted):
        error = {}
        if len(posted['newPassword']) < 1:
            error['newPassword'] = "This field cannot be empty."
        elif len(posted['newPassword']) < 8:
            error['newPassword'] = "Password must be at least 8 characters."
        elif not re.search(r'[A-Z]+', posted['newPassword']):
            error['newPassword'] = "Password must contain an uppercase letter."
        elif not re.search(r'[0-9]+', posted['newPassword']):
            error['newPassword'] = "Password must contain a number."
        if len(posted['confirm']) < 1:
            error['confirm'] = "This field cannot be empty."
        elif posted['confirm'] != posted['newPassword']:
            error['confirm'] = "Password confirmation must match password."
        return error


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    user_level = models.IntegerField()
    password_hash = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=100, default="")
    address_line_2 = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=2, default="")
    zipcode = models.CharField(max_length=10, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    model = models.CharField(max_length=20)
    description = models.CharField(max_length=225)
    image = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.IntegerField()
    quantity = models.IntegerField()
    quantity_sold = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name="products")
    orders = models.ManyToManyField(User, through="OrderDetail", related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    payment_status = models.BooleanField(default=False)
    order_status = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)










