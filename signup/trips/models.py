from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Visit_logs(models.Model):
    name = models.TextField(max_length = 200)
    company = models.TextField(max_length = 200)
    purpose = models.TextField(max_length = 200)
    visit_area = models.TextField(max_length = 200)
    host = models.TextField(max_length = 200, default="")
    signature = models.URLField()
    key = models.TextField(max_length=200, default=0)
    is_out = models.BooleanField(default=True)
    login_time = models.DateTimeField(default=timezone.localtime())
    logout_time = models.DateTimeField(default=timezone.localtime())
    def __str__(self):
        return self.name

class Organizations(models.Model):
	org_name = models.CharField(max_length = 50)
	org_url = models.URLField()
	FAX = models.CharField(max_length = 20)
	def __str__(self):
		return self.org_name
		
class Visitors(models.Model):
	name = models.CharField(max_length = 20)
	phone_number = models.CharField(max_length = 10, default = '0912345678')
	email = models.EmailField(default='example@gmail.com')
	personal_ID = models.CharField(max_length = 10,blank = True)
	org_ID = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.name
