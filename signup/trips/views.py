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
		Name = visitor.name
		Company = visitor.org_ID
		Purpose = request.POST['purpose']
		Signature = request.POST['url']
		Visit_area = request.POST['visit_area']
		Host = request.POST['host']
		Key = request.POST['key']
		Is_out = False
		Login_time = timezone.localtime()
		Logout_time = timezone.localtime()
		#force logout
		try:
			result = Visit_logs.objects.filter(key=Key, is_out=False)
		except Visit_logs.DoesNotExist:
			result = None
		if result:
			print("result")
			Visit_logs.objects.filter(key=Key, is_out=False).update(is_out=True, logout_time=Logout_time)
		#save data
		log = Visit_logs(name=Name, company=Company, purpose=Purpose, visit_area=Visit_area, signature=Signature, host=Host, login_time=Login_time, key=Key, is_out=Is_out)
		log.save()
		print(Name, "key is", Key)
		return HttpResponse(json.dumps({'name': Name}), content_type="application/json")
	return render(request, 'trips/login.html',{})

def addID(request):
	if request.method=="POST":	 
		Name = request.POST['Name']
		Phone_number = request.POST['Phone_number']
		Email = request.POST['Email']
		Personal_ID = request.POST['ID']
		Org_name = request.POST['Org_name']
		if not request.session.session_key:
			request.session.create()	
		request.session['ID'] = Personal_ID
		print("Get Post")
		if request.POST['Org_name']!='':
			org = Organizations.objects.get(org_name=Org_name)
			print("Get exist org")
		if request.POST['OrgName']!='':
			OrgName = request.POST['OrgName']
			Org_url = "https://docs.djangoproject.com/en/2.1/topics/db/queries/"
			FAX = request.POST['FAX']
			org = Organizations(org_name=OrgName, org_url = Org_url, FAX = FAX)
			org.save()
			print("Create org")
		visit = Visitors(name=Name, org_ID=org, phone_number=Phone_number, email=Email, personal_ID=Personal_ID)
		visit.save()
		print("Create visitor")
	all_objects = Organizations.objects.all()
	return render(request, 'trips/addID.html', {'all_objects':all_objects})

def query(request):
	online = Visit_logs.objects.all().filter(is_out = False)
	print(online)
	return render(request, 'trips/query.html' ,{'visit_logs':online})
	
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
			name = result.name
			ID = Visitors.objects.get(name=name).personal_ID
			if ID[-4:] == ID_lastfour:
				check = True
				print(name, "use right qrcode and key is", Key)
				Visit_logs.objects.filter(name=name).update(is_out=True, logout_time=Logout_time)
		print(name, check)
		return HttpResponse(json.dumps({'name': name, 'check': check}), content_type="application/json")
	return render(request, 'trips/logout.html',{})