from django.forms import ModelForm, TextInput, ChoiceField
from .models import Delivery, Payment


class DeliveryForm(ModelForm):
	class Meta:
		model = Delivery
		fields = ['sender_name', 'sender_contact_no', 'sender_email', 'sender_address',
				  'receiver_name', 'receiver_contact_no', 'receiver_email', 'receiver_address', 'description']

		widgets = {
			'sender_name': TextInput(attrs ={
				'class': "form-control"
				}),
			'sender_contact_no': TextInput(attrs ={
				'class': "form-control"
				}),
			'sender_email': TextInput(attrs ={
				'class': "form-control"
				}),
			'sender_address': TextInput(attrs ={
				'class': "form-control"
				}),
			'receiver_name': TextInput(attrs ={
				'class': "form-control"
				}),
			'receiver_contact_no': TextInput(attrs ={
				'class': "form-control"
				}),
			'receiver_email': TextInput(attrs ={
				'class': "form-control"
				}),
			'receiver_address': TextInput(attrs ={
				'class': "form-control"
				}),
			'description': TextInput(attrs ={
				'class': "form-control"
				}),
		}

class PaymentForm(ModelForm):
	class Meta:
		model = Payment
		fields = ['bill_fn', 'bill_sn', 'bill_email', 'pay_method']


		widgets = {
			'bill_fn': TextInput(attrs = {
				'class' : 'form-control'
				}),
			'bill_sn': TextInput(attrs = {
				'class': "form-control"
				}),
			'bill_email': TextInput(attrs = {
				'class': "form-control"
				}),
			'pay_mathod': TextInput(attrs = {
				'class': "form-control"
				}),
		}