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
	if request.method == "POST":
		ID = request.POST['ID']
		if not request.session.session_key:
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
		print("Get visitor name")
		return HttpResponse(json.dumps({'name': name}), content_type="application/json")
	return render(request,'trips/checkID.html',{})

def login(request):
	if request.method == "POST":
		#get request.POST and setup
		ID = request.session['ID']
		visitor = Visitors.objects.get(personal_ID=ID)
		Name = Visitors.objects.get(personal_ID=ID)
		print(Name.org_ID)
		Company = Organizations.objects.get(org_name=Name.org_ID.org_name)
		Purpose = request.POST['purpose']
		Signature = request.POST['url']
		Visit_area = request.POST['visit_area']
		Host = request.POST['host']
		Key = request.POST['key']
		Is_out = False
		Login_time = timezone.localtime()
		Logout_time = Login_time
		print(Login_time==Logout_time)
		#force logout
		try:
			result = Visit_logs.objects.filter(key=Key, is_out=False)
		except Visit_logs.DoesNotExist:
			result = None
		if result:
			print("key")
			Visit_logs.objects.filter(key=Key, is_out=False).update(is_out=True, logout_time=Logout_time)
		try:
			result = Visit_logs.objects.filter(name=Name, is_out=False)
		except Visit_logs.DoesNotExist:
			result = None
		if result:
			print("Name")
			Visit_logs.objects.filter(name=Name, is_out=False).update(is_out=True, logout_time=Logout_time)
		print("here")
		#save data
		log = Visit_logs(name=Name, company=Company, purpose=Purpose, visit_area=Visit_area, signature=Signature, host=Host, login_time=Login_time, key=Key, is_out=Is_out)
		log.save()
		print(Name, "key is", Key)
		return HttpResponse(json.dumps({'name': Name.name}), content_type="application/json")
	return render(request, 'trips/login.html',{})

def addID(request):
	if request.method=="POST":	
		Personal_ID = request.POST['ID']
		Name = request.POST['Name']
		Phone_number = request.POST['Phone_number']
		Email = request.POST['Email']
		Org_name = request.POST['org_Name']
		if not request.session.session_key:
			request.session.create()	
		request.session['ID'] = Personal_ID
		print("Get Post")
		if request.POST['new_Org_Name']=='':
			org = Organizations.objects.get(org_name=Org_name)
			print("Get exist org")
		else:
			new_Org_Name = request.POST['new_Org_Name']
			try:
				result = Organizations.objects.get(org_name=new_Org_Name)
				org = result
				print("org already exist")
			except Organizations.DoesNotExist:
				result = None
				FAX = request.POST['FAX']
				org = Organizations(org_name=new_Org_Name, FAX=FAX)
				org.save()
				print("Create org")
		try:
			exist = Visitors.objects.filter(personal_ID=Personal_ID)
			exist.update(name=Name, org_ID=org, phone_number=Phone_number, email=Email, personal_ID=Personal_ID)
			visit = Visitors.objects.get(personal_ID=Personal_ID)
			print("visitor already exist")
		except Visitors.DoesNotExist:
			visit = Visitors(name=Name, org_ID=org, phone_number=Phone_number, email=Email, personal_ID=Personal_ID)
			visit.save()
			print("Create visitor")
	all_objects = Organizations.objects.all()
	return render(request, 'trips/addID.html', {'all_objects':all_objects})

def logout(request):
	if request.method == "POST":
		Logout_time = timezone.localtime()
		Key = request.POST['key']
		ID_lastfour = request.POST['ID']
		name = "Not found"
		check = False
		try: 
			result = Visit_logs.objects.get(key=Key, is_out=False)
		except Visit_logs.DoesNotExist:
			result = None
		if result:
			Name = result.name
			ID = Name.personal_ID
			if not request.session.session_key:
				request.session.create()	
			request.session['ID'] = ID
			if ID[-4:] == ID_lastfour:
				check = True
				print(Name.name, "use right qrcode and key is", Key)
				log = Visit_logs.objects.filter(name=Name).order_by('-login_time')[0]
				log.logout_time = Logout_time
				log.is_out = True
				log.save()
				name = Name.name
		print(name,check)
		return HttpResponse(json.dumps({'name': name, 'check': check}), content_type="application/json")
	return render(request, 'trips/logout.html',{})

def confirm(request):
	ID = request.session['ID']
	name = Visitors.objects.get(personal_ID=ID)
	try: 
		result = Visit_logs.objects.get(name=name, is_out=False)
	except Visitors.DoesNotExist:
		result = None
	return render(request, 'trips/confirm.html',{'result':result})

def logout_confirm(request):
	ID = request.session['ID']
	name = Visitors.objects.get(personal_ID=ID)
	try: 
		result = Visit_logs.objects.filter(name=name).order_by('-logout_time')[0]
		print(result)
	except Visitors.DoesNotExist:
		result = None
	return render(request, 'trips/confirm.html',{'result':result})



