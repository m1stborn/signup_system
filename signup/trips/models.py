from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class visitor(models.Model):
    name = models.TextField(max_length = 200)
    company = models.TextField(max_length = 200)
    visit_area = models.TextField(max_length = 200)
    purpose = models.TextField(max_length = 200)
    login_time = models.DateTimeField('Enter time',default=timezone.localtime())
    logout_time = models.DateTimeField(auto_now_add=True)
    signature = models.URLField()
    def __str__(self):
        return self.name