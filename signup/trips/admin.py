from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea,DateTimeInput
from .models import Visit_logs, Visitors, Organizations
from django.contrib.admin import DateFieldListFilter
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
	
	date_hierarchy = 'login_time'
	ordering = ('-login_time',)
	search_fields = ('name','company',)
	list_display = ('name' ,'login_time','logout_time','is_out')
	list_editable = ('login_time','logout_time')
	list_filter = ('company','logout_time','is_out')

	actions = ['make_out']

	def make_out(self, request, queryset):
		queryset.update(is_out=True)
	make_out.short_description = "訪客登出"
	# readonly_fields = ['company','visit_area','purpose','login_time','host']

admin.site.register(Visit_logs,Visit_logAdmin)