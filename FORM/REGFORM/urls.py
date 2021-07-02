from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutcovid19', views.aboutcovid19, name='aboutcovid19'),
    path('symptom', views.symptoms, name='symptom'),
    path('precaution', views.precaution, name='precaution'),
    path('treatment', views.treatment, name='treatment'),
    path('vaccine', views.vaccine, name='vaccine'),
    path('pakistancases', views.pakistancases, name='pakistancases'),
    path('registrationform', views.registrationform, name='registrationform'),
    path('complaintform', views.complaintform, name='complaintform'),
]
