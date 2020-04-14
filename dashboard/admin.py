from django.contrib import admin

from .models import WorkExperience, Education, Skills


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_year', 'end_year', 'actual_job']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', 'school_name', 'start_year', 'end_year']


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
