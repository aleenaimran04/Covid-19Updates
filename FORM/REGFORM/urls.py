from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guidance', views.guidance, name='guidance'),
    path('pakistancases', views.pakistancases, name='pakistancases'),
    path('worldwidecases', views.worldwidecases, name='worldwidecases'),
    path('registrationform', views.registrationform, name='registrationform'),
    path('complaintform', views.complaintform, name='complaintform'),
    path('registrationform/Api/create/', views.createapi),
    path('complaintform/Api/create/', views.CreateApi),
]