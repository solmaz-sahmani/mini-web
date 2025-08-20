from django.urls import path
from . import views

app_name = 'contactus_api_v1'

urlpatterns = [
    path('v1/', views.contactus_api_v1, name='contactus_apiv1'),
]