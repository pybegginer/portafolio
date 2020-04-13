from django.contrib import admin

from .models import WorkExperience


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_year', 'end_year', 'actual_job']
