from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import DeliveryForm, PaymentForm
from .filters import DeliveryFilter, PaymentFilter
from django.contrib import messages

# Create your views here.
def index(request):
	context= {}
	return render (request, 'cms/index.html',context)

#logged in user only
def dashboard(request):
	context = {}
	return render(request, 'cms/dashboard.html', context)

#logged in user only
def tracking(request):
	delivery = Delivery.objects.all()
	payment = Payment.objects.all()

	myFilter = DeliveryFilter(request.GET, queryset=delivery)
	delivery = myFilter.qs

	context = {'delivery': delivery, 'myFilter': myFilter, 'payment': payment}
	return render(request, 'cms/tracking.html', context)

def login(request):
	context= {}
	return render(request, 'cms/login.html',context)

#logged in user only
def payment(request):
	
	payment = Payment.objects.all()
	form = PaymentForm()


	if request.method == 'POST': 
		#print('Printing POST:', request.POST)
		form = PaymentForm(request.POST)
		if request.POST.get('pay_method') == 'COD':
			if form.is_valid():
				if Payment.objects.filter(shipment=request.POST['shipment']).exists():
					messages.error(request, 'Transaction already exists')
					return redirect('payment')
				else:
					form.save()

				return redirect('pay_tables')

		if request.POST.get('pay_method') == 'Credit Card':
			if form.is_valid():
				if Payment.objects.filter(shipment=request.POST['shipment']).exists():
					messages.error(request, 'Transaction already exists')
					return redirect('payment')
				else:
					form.save()

				return redirect('pay_tables')

		if request.POST.get('pay_method') == 'Paypal':
			if form.is_valid():
				if Payment.objects.filter(shipment=request.POST['shipment']).exists():
					messages.error(request, 'Transaction already exists')
					return redirect('payment')
				else:
					form.save()

				return redirect('pay_tables')

	context= {'form':form, 'payment':payment}
	return render(request, 'cms/payment.html',context)

#logged user in only
def updatepayment(request, pk):
	payment = Payment.objects.get(transaction_id=pk)
	form = PaymentForm(instance=payment)

	if request.method == 'POST': 
		#print('Printing POST:', request.POST)
		form = PaymentForm(request.POST, instance=payment)
		if form.is_valid():
			form.save()

			return redirect('pay_tables')

	context= {'form':form, 'payment': payment}
	return render(request, 'cms/updatepayment.html',context)

#logged in user only
def delivery(request):
	form = DeliveryForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = DeliveryForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('tracking')

	context= {'form': form}
	return render(request, 'cms/delivery.html', context)

#logged in user only
def updatedelivery(request, pk):
	
	delivery = Delivery.objects.get(id=pk) 
	form = DeliveryForm(instance=delivery)

	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = DeliveryForm(request.POST, instance=delivery)
		if form.is_valid():
			form.save()
			return redirect('tracking') 

	context = {'form': form}
	return render(request, 'cms/delivery.html', context)

#logged in user only
def deletedelivery(request, pk):
	delivery = Delivery.objects.get(id=pk)
	if request.method == "POST":
		delivery.delete()
		return redirect('tracking') 

	context = {'item':delivery}
	return render(request, 'cms/delete.html', context)



def displaytracking(request):
	delivery = Delivery.objects.all()

	context = {'delivery': delivery}
	return render(request, 'cms/displaytracking.html', context)

#logged in user only
def pay_tables(request):
	payment = Payment.objects.all()

	payfilter = PaymentFilter(request.GET, queryset=payment)
	payment = payfilter.qs

	context = {'payment': payment, 'payfilter':payfilter}
	return render(request, 'cms/pay_tables.html',  context)

def result(request):
	if request.method == "POST":
		trackingid = request.POST['trackingid']
		trackid = Delivery.objects.filter(id__contains=trackingid)

		context = {'trackingid':trackingid, 'trackid':trackid}
		return render(request, 'cms/result.html', context)
	else:

		context = {}
		return render(request, 'cms/result.html', context)

def details(request, pk):
	delivery = Delivery.objects.get(id=pk)

	context = {'delivery':delivery}
	return render(request, 'cms/details.html', context	)
