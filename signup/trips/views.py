from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Visit_logs, Visitors, Organizations
from datetime import datetime
from django.template import RequestContext
import django.utils.timezone as timezone
import json

# Create your views here.
def home(request):
	return render(request, 'trips/home.html', {})

def checkID(request):
	if request.method == "POST": #os request.GET()
		ID = request.POST['ID']
		if not request.session.session_key:
			print('create session_key')
			request.session.create()		
		request.session['ID'] = ID
		try: 
			result = Visitors.objects.get(personal_ID=ID)
		except Visitors.DoesNotExist:
			result = None
		if result:
			name = result.name	
		else:
			name = "Not found"
		return HttpResponse(json.dumps({'name': name}), content_type="application/json")
	return render(request,'trips/checkID.html',{})

def login(request):
	print("123")
	if request.method == "POST":
		print("1")
		ID = request.session['ID']
		visitor = Visitors.objects.get(personal_ID=ID)
		Name = visitor.name
		Company = visitor.org_ID
		Purpose = request.POST['purpose']
		Signature = request.POST['url']
		Visit_area = request.POST['visit_area']
		Login_time = timezone.localtime()
		Key = request.POST['key']
		Is_out = False
		log = Visit_logs(name=Name, company=Company, purpose=Purpose, visit_area=Visit_area, signature=Signature, login_time=Login_time, key=Key, is_out=Is_out)
		log.save()
	return render(request, 'trips/login.html',{})

def addID(request):
	if request.method=="POST":
		Name = request.POST['Name']
		Phone_number = request.POST['Phone_number']
		Email = request.POST['Email']
		Personal_ID = request.session['ID']
		Org_name = request.POST['Org_name']
		Org_url = request.POST['Url']
		FAX = request.POST['Fax']
		org = Organizations(org_name=Org_name, org_url=Org_url, FAX=FAX)
		org.save()
		visit = Visitors(name=Name, org_ID=org, phone_number=Phone_number, email=Email, personal_ID=Personal_ID)
		visit.save()

		# return render(request,'trips/login.html',{})
		return redirect('login')
	return render(request, 'trips/addID.html', {})

def logout(request):
	print("out")
	if request.method == "POST":
		Logout_time = timezone.localtime()
		Key = request.POST['key']
		queryset = Visit_logs.objects.filter(key=Key, is_out=False).order_by('-login_time')
		Visit_logs.objects.filter(pk=queryset[0].pk).update(is_out=True, logout_time=Logout_time)
	return render(request, 'trips/logout.html',{})

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
