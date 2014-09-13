from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.

class Member(models.Model):
	phone_number = PhoneNumberField()
	created_on = models.DateTimeField(default = datetime.now())

class Business(models.Model):
	created_on = models.DateTimeField(default = datetime.now())
	name = models.CharField(max_length = 50)
	phone_number = PhoneNumberField()


class Credit(models.Model):
	created_on = models.DateTimeField(default = datetime.now())
	member = models.ForeignKey('Member')
	business = models.ForeignKey('Business')
	balance = models.DecimalField(decimal_places = 2, max_digits = 20)

class Transaction(models.Model):
	amount = models.DecimalField(decimal_places = 2, max_digits = 20)
	created_on = models.DateTimeField(default = datetime.now())
	member = models.ForeignKey('Member')
	business = models.ForeignKey('Business')
	verified = models.BooleanField(default = False)