from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea,DateTimeInput
from .models import Visit_logs, Visitors, Organizations
from django.contrib.admin import DateFieldListFilter
from daterange_filter.filter import DateRangeFilter
import django.utils.timezone as timezone
import csv
from django.http import HttpResponse
# admin.site.register(Visit_logs)

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([str(getattr(obj, field)) for field in field_names])

        return response

    export_as_csv.short_description = "將所選的訪客紀錄輸出"

class VisitorAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'20'})},
		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
		# models.DateTimeField: {'widget':DateTimeInput(attrs={'rows':1, 'cols':20})}
	}
	list_filter = ('company',)
admin.site.disable_action('delete_selected')

class VisitorsAdmin(admin.ModelAdmin,ExportCsvMixin): 
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'20'})},
		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
		# models.DateTimeField: {'widget':DateTimeInput(attrs={'rows':1, 'cols':20})}
	}
	search_fields = ('name','org_ID__org_name',)
	list_display = ('name' ,'phone_number','org_ID')
	list_filter = ('org_ID',)
	fields = ('name' ,'phone_number','email','personal_ID','org_ID')
	actions = ['export_as_csv']
	# def has_delete_permission(self, request, obj=None):
	# 	return False
admin.site.register(Visitors, VisitorsAdmin)



class OrganizationsAdmin(admin.ModelAdmin,ExportCsvMixin): 
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'20'})},
		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
		# models.DateTimeField: {'widget':DateTimeInput(attrs={'rows':1, 'cols':20})}
	}
	search_fields = ('org_name',)
	list_display = ('org_name',)
	fields = ('org_name' ,'FAX')
	actions = ['export_as_csv']
	# def has_delete_permission(self, request, obj=None):
	# 	return False
admin.site.register(Organizations, OrganizationsAdmin)
# Register your models here.




class Visit_logAdmin(admin.ModelAdmin,ExportCsvMixin):
	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'20'})},
		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':10})},
		# models.DateTimeField: {'widget':DateTimeInput(attrs={'rows':1, 'cols':20})}
	}
	
	# date_hierarchy = 'login_time'
	ordering = ('-login_time',)
	# search_fields = ('name','company',)
	list_display = ('name' ,'company','login_time','logout_time','key','is_out','is_confirm')
	# list_editable = ('login_time','logout_time')
	list_filter = (('login_time',(DateRangeFilter)),'is_out','host')
	readonly_fields = ('name','company',)
	fields = ('name','company','purpose','visit_area','host','key','is_out','login_time','logout_time','is_confirm','host_key','alter_key')
	
	# exclude = ('signature',)
	actions = ['make_logs_out','export_as_csv','confirm_logs']

	def make_logs_out(self, request, queryset):
		queryset.update(is_out=True, logout_time=timezone.localtime())
	make_logs_out.short_description = "將所選的訪客紀錄簽退"
	
	def confirm_logs(self, request, queryset):
		queryset.update(is_confirm=True)
	confirm_logs.short_description = "確認所選的訪客紀錄"
	# def has_delete_permission(self, request, obj=None):
	# 	return False
	# readonly_fields = ['company','visit_area','purpose','login_time','host']
	class Media:
		js = ("autorefresh.js",)
admin.site.register(Visit_logs,Visit_logAdmin)
# admin.sites.AdminSite.site_url = "http://localhost:8000/admin/trips/visit_logs/?drf__login_time__gte=2018-11-28&drf__login_time__lte="