from django.shortcuts import render

# Create your views here.
def index(request):
	context = {}
	return render(request, 'cms/index.html', context)

def add_goods(request):
	context = {}
	return render(request, 'cms/add_goods.html', context)

def dashboard(request):
	context = {}
	return render(request, 'cms/dashboard.html', context)

def good_records(request):
	context = {}
	return render(request, 'cms/good_records.html', context)

def register(request):
	context = {}
	return render(request, 'cms/register.html', context)

def tracking(request):
	context = {}
	return render(request, 'cms/tracking.html', context)