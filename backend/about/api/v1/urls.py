from django.urls import path
from . import views

app_name = 'about_api_v1'

urlpatterns = [
    path('v1/', views.about_api_v1, name='about_apiv1'),
]