from django.db import models
from django.forms import ModelForm
import datetime
from uuid import uuid4
# Create your models here.

def create_id():
	now = datetime.datetime.now()
	return str(now.year) + str(now.month) + str(now.day) + str(uuid4())[:7]


class Customers(models.Model):
	name = models.CharField(max_length = 200, null = True)
	username = models.CharField(max_length = 200, null = True)
	password = models.CharField(max_length = 8, null = True)
	mobile_no = models.CharField(max_length = 200, null = True)
	email = models.CharField(max_length = 200, null = True)
	address = models.CharField(max_length = 200, null =True)
	dob = models.DateField()

	def __str__(self):
		return self.name

class Delivery(models.Model):
	sender_name = models.CharField(max_length = 200, null = True)
	sender_contact_no = models.CharField(max_length = 200, null = True)
	sender_email = models.CharField(max_length = 200, null = True)
	sender_address = models.CharField(max_length = 200, null = True)
	receiver_name = models.CharField(max_length = 200, null = True)
	receiver_contact_no = models.CharField(max_length = 200, null = True)
	receiver_email = models.CharField(max_length = 200, null = True)
	receiver_address = models.CharField(max_length = 200, null = True)
	description = models.CharField(max_length = 200, null = True)
	id = models.CharField(primary_key = True, default = create_id, editable = False, max_length = 10)

	def __str__(self):
		return self.id

class Payment(models.Model):
	STATUS = (('Pending','Pending'),
			 ('Paid', 'Paid'))
	METHOD = (('COD','COD'),
			  ('Credit Card','Credit Card'),
			  ('Paypal','Paypal'))

	shipment = models.ForeignKey(Delivery, null = True, on_delete = models.SET_NULL)
	bill_fn = models.CharField(max_length = 200, null = True)
	bill_sn = models.CharField(max_length = 200, null = True)
	bill_email = models.CharField(max_length = 200, null = True)
	price = models.FloatField(default = 500)
	pay_method = models.CharField(max_length = 11, null = True, choices = METHOD)
	pay_status = models.CharField(max_length = 11, choices = STATUS, default= 'Pending')
	
	def __str__(self):
		return self.shipment


	
		