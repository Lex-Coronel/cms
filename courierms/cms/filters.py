import django_filters
from .models import *
from django_filters import CharFilter

class DeliveryFilter(django_filters.FilterSet):
	#id = CharFilter(lookup_expr = 'icontains')

	class Meta:
		model = Delivery
		fields = ['id']

class PaymentFilter(django_filters.FilterSet):
	class Meta:
		model = Payment
		fields = ['transaction_id']