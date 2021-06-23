from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
	context= {}
	return render (request, 'index.html',context)

def tracking(request):
	context= {}
	return render(request, 'tracking.html',context)

def login(request):
	context= {}
	return render(request, 'login.html',context)

def payment(request):
	context= {}
	return render(request, 'payment.html',context)

def dashboard(request):
	context= {}
	return render(request, 'dashboard.html',context)

def delivery(request):
	context= {}
	return render(request, 'delivery.html',context)

def displaytracking(request):
	context= {}
	return render(request, 'displaytracking.html',context)
