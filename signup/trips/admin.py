from django.contrib import admin
from .models import visit_log, Visitor, Organization
admin.site.register(visit_log)
admin.site.register(Visitor)
admin.site.register(Organization)
# Register your models here.
