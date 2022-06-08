from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('doctorpage/', views.doctor, name='doctorpage'),
    path('patient/', views.patient, name='patient'),
]