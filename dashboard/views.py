from django.shortcuts import render
from django.views import View  # Clase basada en vista

from .models import WorkExperience, Education, Skills


class Index(View):
    def get(self, request):
        template_name = 'index.html'
        context = dict(
        	works=WorkExperience.objects.all(),
        	education=Education.objects.all(),
        	skills = Skills.objects.all(),
        	)
        return render(request, template_name, context)

class WorkExperienceView(View):
	def get(self,request):
		template_name = 'works.html'
		context = dict(
			works = WorkExperience.objects.all(),
			)
		return render(request,template_name,context)

class EducationView(View):
	def get(self,request):
		template_name = 'education.html'
		context = dict(
			educations = Education.objects.all(),
			)
		return render(request,template_name,context)

class SkillsView(View):
	def get(self,request):
		template_name = 'skills.html'
		context = dict(
			skills = Skills.objects.all(),
			)
		return render(request,template_name,context)