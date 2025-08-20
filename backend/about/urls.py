from django.urls import path, include
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    path('api/', include('about.api.v1.urls')),
]