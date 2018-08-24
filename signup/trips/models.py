from django.db import models

# Create your models here.
class visitor(models.Model):
    name = models.TextField(max_length = 200)
    company = models.TextField(max_length = 200)
    visit_area = models.TextField(max_length = 200)
    purpose = models.TextField(max_length = 200)
    login_time = models.DateTimeField('Enter time')
    logout_time = models.DateTimeField('Exit time')
    def __str__(self):
        return self.name