from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('monitor/', views.traffic_monitor, name="monitor"), #system monitor view to be created next
]