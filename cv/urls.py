from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import Index, SkillsView, EducationView, WorkExperienceView
urlpatterns = [
    path('admin/', admin.site.urls),
    #  Siempre que usemos clases basadas en vista debemos utilizar el método .as_view() de la clase.
    path('', Index.as_view(), name= 'index'),
    path('habilidades', SkillsView.as_view(), name = 'habilidades'),
    path('experiencia', WorkExperienceView.as_view(), name= 'experiencia'),
    path('educacion',EducationView.as_view(), name='educacion'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) #para que Django entienda que son medias que va a traer

