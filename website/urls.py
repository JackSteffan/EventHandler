from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),

]
