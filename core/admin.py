from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    
admin.site.register(Project, ProjectAdmin)

admin.site.site_title = "Asif Ekbal"
admin.site.site_header = "Personal Website Admin Panel"
admin.site.index_title = "Admin Area"


