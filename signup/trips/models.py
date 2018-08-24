from django.db import models

# Create your models here.
class visitor(models.Model):
    name = models.TextField(max_length = 50, blank = True)
    company = models.TextField(max_length = 50, blank = True)
    visit_area = models.TextField(max_length = 50, blank = True)
    purpose = models.TextField(max_length = 50, blank = True)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name