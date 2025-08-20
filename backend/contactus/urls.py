from django.urls import path, include
from . import views

app_name = 'contactus'

urlpatterns = [
    path('', views.contactus, name='contactus'),
    path('api/', include('contactus.api.v1.urls')),
]