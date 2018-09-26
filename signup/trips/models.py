from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class visit_log(models.Model):
    name = models.TextField(max_length = 200)
    company = models.TextField(max_length = 200)
    purpose = models.TextField(max_length = 200)
    visit_area = models.TextField(max_length = 200)
    signature = models.URLField()
    key = models.TextField(max_length=200, default=0)
    is_out = models.BooleanField(default=True)
    login_time = models.DateTimeField(default=timezone.localtime())
    logout_time = models.DateTimeField(default=timezone.localtime())
    def __str__(self):
        return self.name

class Organization(models.Model):
	org_name = models.TextField(max_length = 200)
	org_url = models.URLField()
	FAX = models.IntegerField()
	def __str__(self):
		return self.org_name
		
class Visitor(models.Model):
	name = models.TextField(max_length = 200)
	phone_number = models.IntegerField(unique=True, null = True)
	email = models.EmailField(default='example@gmail.com')
	personal_ID = models.TextField(max_length = 10,blank = True)
	org_ID = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.name
