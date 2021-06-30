import django_filters
from .models import *
from django_filters import CharFilter

class DeliveryFilter(django_filters.FilterSet):
	id = CharFilter(lookup_expr = 'icontains')

	class Meta:
		model = Delivery
		fields = ['id']

