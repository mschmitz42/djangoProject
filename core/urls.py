from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.core_index, name='core_index'),
    path('about', views.core_about, name='core_about'),
    path('scheduler', views.core_scheduler, name='core_scheduler'),
    path('profile', views.core_profile, name='core_profile'),
]
