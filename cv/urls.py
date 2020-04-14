from django.contrib import admin
from django.urls import path

from dashboard.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    #  Siempre que usemos clases basadas en vista debemos utilizar el método .as_view() de la clase.
    path('', Index.as_view()),
]
