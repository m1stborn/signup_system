from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .models import visitor
from datetime import datetime
from .forms import VisitorForm
from django.template import RequestContext
import django.utils.timezone as timezone
import json

# Create your views here.

def home(request):
	return render(request, 'trips/home.html', {})

def new(request):
	if request.method == "POST":
		Name = request.POST['name']
		Company = request.POST['company']
		Purpose = request.POST['purpose']
		url = request.POST['url']
		visit_area = request.POST['visit_area']
		getImg = visitor(signature = url, name=Name, company=Company, purpose=Purpose)
		getImg.save()
	all_objects = visitor.objects.all().order_by('name')
	print(request.user)
	return render(request, 'trips/enter.html',{'all_obbjects':all_objects})

def Q_in(request):
	print("come")
	if request.method == "POST":
		print(request.user)
		print(request.POST['key'])
	return render(request, 'trips/test3.html',{})

def Q_out(request):
	print("out")
	if request.method == "GET":
		print(request.GET)
	return render(request, 'trips/test3.html',{})

# def getImg(request):
# 	if request.method == "POST":
# 		Name = form.cleaned_data['Name']
#         Company = form.cleaned_data['Company']
#         Purpose = form.cleaned_data['Purpose']
# 		str=json.dumps(request.POST).split('"')
# 		getImg = vistor(signature = str[3],name=Name, company=Company, purpose=Purpose)
# 		getImg.save()
# 	return render(request, 'trips/byid.html',{})

# def new(request):ya
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = VisitorForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             Name = form.cleaned_data['Name']
#             Company = form.cleaned_data['Company']
#             Purpose = form.cleaned_data['Purpose']
#             new = visitor(name=Name, company=Company, purpose=Purpose)
#             new.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect('/Q_in/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = VisitorForm()

#     return render(request, 'trips/enter.html', {'form': form})

# def new(request):
# 	if 'code' in request.GET:
# 		print(request.GET['code'])
# 		print("in")
# 		# Name = request.GET['Name']
# 		# Company = request.GET['Company']
# 		# Purpose = request.GET['Purpose']
# 		# new = visitor(name=Name, company=Company, purpose=Purpose)
# 		# new.save()
# 		return redirect('hello_world')
# 	return render(request, 'trips/test3.html', {})

# def getImg(request):
# 	file_content = ContentFile(request.FILES['img'].read())
# 	img = ImageStore(name = request.FILES['img'].name, img = request.FILES['img'])
# 	img.save()


# def new(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             print(form);
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'trips/enter.html', {'form': form})



# def my_view(request):
#     form = SignatureForm(request.POST or None)
#     if form.is_valid():
#         signature = form.cleaned_data.get('signature')
#         if signature:
#             # as an image
#             signature_picture = draw_signature(signature)
#             # or as a file
#             signature_file_path = draw_signature(signature, as_file=True)
