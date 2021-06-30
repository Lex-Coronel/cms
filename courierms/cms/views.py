from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import DeliveryForm, PaymentForm

# Create your views here.
def index(request):
	context= {}
	return render (request, 'cms/index.html',context)

def tracking(request):
	delivery = Delivery.objects.all()

	return render(request, 'cms/tracking.html', {'delivery': delivery})

def login(request):
	context= {}
	return render(request, 'cms/login.html',context)

def payment(request):
	form = PaymentForm()

	if request.method == 'POST': 
		#print('Printing POST:', request.POST)
		form = PaymentForm(request.POST)
		if request.POST.get('pay_method') == 'COD':
			if form.is_valid():
				form.save()

				return redirect('pay_tables')

		if request.POST.get('pay_method') == 'Credit Card':
			if form.is_valid():
				form.save()

				return redirect('cc_payment/shipment/')

		if request.POST.get('pay_method') == 'Paypal':
			if form.is_valid():
				form.save()

				return redirect('pay_tables')

	context= {'form':form}
	return render(request, 'cms/payment.html',context)

def updatepayment(request, pk):
	payment = Payment.objects.get(shipment=pk)
	form = PaymentForm(instance=payment)

	if request.method == 'POST': 
		#print('Printing POST:', request.POST)
		form = PaymentForm(request.POST, instance=payment)
		if form.is_valid():
			form.save()

			return redirect('pay_tables')

	context= {'form':form}
	return render(request, 'cms/payment.html',context)


def dashboard(request):
	context= {}
	return render(request, 'cms/dashboard.html',context)

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

def deletedelivery(request, pk):
	delivery = Delivery.objects.get(id=pk)
	if request.method == "POST":
		delivery.delete()
		return redirect('tracking') 

	context = {'item':delivery}
	return render(request, 'cms/delete.html', context)



def displaytracking(request):
	context= {}
	return render(request, 'cms/displaytracking.html',context)


def pay_tables(request):
	payment = Payment.objects.all()

	return render(request, 'cms/pay_tables.html',  {'payment': payment})
