from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def hello_world(request):
	return HttpResponse("Hello world!")