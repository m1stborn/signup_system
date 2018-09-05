from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class visitor(models.Model):
    name = models.TextField(max_length = 200)
    company = models.TextField(max_length = 200)
    purpose = models.TextField(max_length = 200)
    visit_area = models.TextField(max_length = 200)
    signature = models.URLField()
    key = models.TextField(max_length=200, default=0)
    is_out = models.BooleanField(default=True)
    login_time = models.DateTimeField(default=0)
    logout_time = models.DateTimeField(default=0)
    def __str__(self):
        return self.name