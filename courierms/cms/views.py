from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import DeliveryForm

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
	context= {}
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
			return redirect('payment')

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


