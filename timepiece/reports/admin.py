from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from timepiece.reports.models import Report

class ReportAdmin(GuardedModelAdmin):
    list_display = ('name', 'slug', 'url_name', 'nav_option', )

admin.site.register(Report, ReportAdmin)
