from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('profile/', views.profile, name='profile'),
    path('event/create/', views.EventCreate.as_view(), name='event-create'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('role/create/', views.RoleCreate.as_view(), name='role-create'),
    path('role/<uuid:pk>', views.RoleDetailView.as_view(), name='role-detail'),
]
