from django.shortcuts import render
from django.views import View  # Clase basada en vista

from .models import WorkExperience, Education, Skills


class Index(View):
    def get(self, request):
        template_name = 'index.html'
        works = WorkExperience.objects.all()  # Django Queryset - Trae todos los objetos.
        context = dict(works=works)
        return render(request, template_name, context)
