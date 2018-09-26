from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .models import visit_log
from datetime import datetime
from django.template import RequestContext
import django.utils.timezone as timezone
import json

# Create your views here.

def home(request):
	return render(request, 'trips/home.html', {})

def login(request):
	if request.method == "POST":
		# print(request.POST)
		Name = request.POST['name']
		Company = request.POST['company']
		Purpose = request.POST['purpose']
		Url = request.POST['url']
		Visit_area = request.POST['visit_area']
		Login_time = timezone.localtime()
		Key = request.POST['key']
		Is_out = False
		getImg = visit_log(name=Name, company=Company, purpose=Purpose, visit_area=Visit_area, signature=Url, login_time=Login_time, key=Key, is_out=Is_out)
		getImg.save()
		# thisobject = visitor.objects.get(login_time=Login_time).pk
		# print(thisobject)
		# return render(request, 'trips/test3.html',{'object':thisobject})
	all_name = visit_log.objects.values('name').distinct()
	all_company = visit_log.objects.values('company').distinct()
	all_purpose = visit_log.objects.values('purpose').distinct()
	# print(visitor.objects.all().count())
	return render(request, 'trips/big.html',{'all_name':all_name,'all_company':all_company,'all_purpose':all_purpose})

def logout(request):
	print("out")
	if request.method == "POST":
		Logout_time = timezone.localtime()
		Key = request.POST['key']
		queryset = visit_log.objects.filter(key=Key, is_out=False).order_by('-login_time')
		# a = visitor.objects.filter(login_time__year='2018')
		# print(a)
		# b = visitor.objects.filter(login_time__year='2018', login_time__month='09', login_time__date='')
		# print(b)
		print(queryset[0])
		visit_log.objects.filter(pk=queryset[0].pk).update(is_out=True, logout_time=Logout_time)
	return render(request, 'trips/test3.html',{})


# def Q_in(request):
# 	print("come")
# 	if request.method == "POST":
# 		print(request.POST['pk'])
# 		print(request.POST['key'])
# 	return render(request, 'trips/test3.html',{})



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
