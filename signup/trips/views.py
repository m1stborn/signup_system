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
	return render(request, 'trips/signiture.html', {})

def getImg(request):
	file_content = ContentFile(request.FILES['img'].read())
	img = ImageStore(name = request.FILES['img'].name, img = request.FILES['img'])
	img.save()


def upload_image_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # HCC identification
            # 1.跑 vgg 16 model
            # 2.儲存辨識後的影像(?)<--看 vgg16 model 的 output 是什麼
            # 3.如果 predict 的時間較久，前端要顯示一下相關訊息

            return HttpResponseRedirect(reverse('medical_images'))
    else:
        form = UploadForm()
    return render(request, 'board/medicalimage_form.html', {'form': form})
