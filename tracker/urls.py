from django.urls import path
from tracker import views

app_name = 'tracker'

urlpatterns = [
    path('', views.tracker_index, name='tracker_index'),
    path('dashboard', views.tracker_dashboard, name='tracker_dashboard'),
]