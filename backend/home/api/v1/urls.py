from django.urls import path
from . import views

app_name = 'home_api_v1'

urlpatterns = [
    path('v1/', views.home_api_v1, name='home_apiv1'),
]