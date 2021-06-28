from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
	context= {}
	return render (request, 'cms/index.html',context)

def tracking(request):
	context= {}
	return render(request, 'cms/tracking.html',context)

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
	context= {}
	return render(request, 'cms/delivery.html',context)

def displaytracking(request):
	context= {}
	return render(request, 'cms/displaytracking.html',context)
