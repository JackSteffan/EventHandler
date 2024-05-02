from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('profile/', views.profile, name='profile'),
]
