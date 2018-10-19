from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea,DateTimeInput
from .models import Visit_logs, Visitors, Organizations
# admin.site.register(Visit_logs)
admin.site.register(Visitors)
admin.site.register(Organizations)
# Register your models here.
class Visit_logAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'20'})},
		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
		# models.DateTimeField: {'widget':DateTimeInput(attrs={'rows':1, 'cols':20})}
	}
	list_display = ('name' , 'company' , 'visit_area','purpose','login_time')
	list_editable = ('company' , 'login_time','visit_area','purpose')
	list_filter = ('company',)

admin.site.register(Visit_logs,Visit_logAdmin)