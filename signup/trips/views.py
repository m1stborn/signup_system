from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from .models import visitor
from datetime import datetime
# Create your views here.

def hello_world(request):
	return HttpResponse("Hello world!")



def new(request):
	if 'Name' and 'Company' and 'Purpose' in request.GET:
		print("in")
		Name = request.GET['Name']
		Company = request.GET['Company']
		Purpose = request.GET['Purpose']
		new = visitor(name=Name, company=Company, purpose=Purpose)
		new.save()
		# return redirect('new')
	return render(request, 'trips/enter.html',{})

def getImg(request):
	file_content = ContentFile(request.FILES['img'].read())
	img = ImageStore(name = request.FILES['img'].name, img = request.FILES['img'])
	img.save()

def qrcode(request):
	# return HttpResponse("Hello world!")
	# return render_to_response('trips/test2.html')
	return render(request,'trips/test2.html',{})