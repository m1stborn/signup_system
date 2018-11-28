from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea,DateTimeInput
from .models import Visit_logs, Visitors, Organizations
from django.contrib.admin import DateFieldListFilter
from daterange_filter.filter import DateRangeFilter
# admin.site.register(Visit_logs)


# class VisitorAdmin(admin.ModelAdmin):
# 	formfield_overrides = {
# 		models.CharField: {'widget': TextInput(attrs={'size':'20'})},
# 		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
# 		# models.DateTimeField: {'widget':DateTimeInput(attrs={'rows':1, 'cols':20})}
# 	}
# 	list_filter = ('company',)



admin.site.register(Visitors)
admin.site.register(Organizations)
# Register your models here.

class Visit_logAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'20'})},
		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
		# models.DateTimeField: {'widget':DateTimeInput(attrs={'rows':1, 'cols':20})}
	}
	
	# date_hierarchy = 'login_time'
	ordering = ('-login_time',)
	# search_fields = ('name','company',)
	list_display = ('name' ,'company','login_time','logout_time','is_out')
	# list_editable = ('login_time','logout_time')
	list_filter = (('login_time'),'is_out','host')
	readonly_fields = ('name','company',)
	fields = ('name','company','purpose','visit_area','host','key','is_out','login_time','logout_time',)
	# exclude = ('signature',)
	actions = ['make_out']

	def make_out(self, request, queryset):
		queryset.update(is_out=True)
	make_out.short_description = "登出所選的 訪客紀錄"
	# readonly_fields = ['company','visit_area','purpose','login_time','host']
	class Media:
		js = ("autorefresh.js",)
admin.site.register(Visit_logs,Visit_logAdmin)
# admin.sites.AdminSite.site_url = "http://localhost:8000/admin/trips/visit_logs/?drf__login_time__gte=2018-11-28&drf__login_time__lte="