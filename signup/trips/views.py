from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import visitor
from datetime import datetime
# Create your views here.

def hello_world(request):
	return render(request, 'trips/home.html', {})



def new(request):
	if 'Name' and 'Company' and 'Purpose' in request.GET:
		print("in")
		Name = request.GET['Name']
		Company = request.GET['Company']
		Purpose = request.GET['Purpose']
		new = visitor(name=Name, company=Company, purpose=Purpose)
		new.save()
		return redirect('hello_world')
	return render(request, 'trips/enter.html', {})

def getImg(request):
	file_content = ContentFile(request.FILES['img'].read())
	img = ImageStore(name = request.FILES['img'].name, img = request.FILES['img'])
	img.save()