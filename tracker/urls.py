from django.urls import path
from tracker import views

app_name = 'tracker'

urlpatterns = [
    # path('', views.tracker_index, name='tracker_index'),
    path('', views.tracker_index, name='tracker_index'),
]