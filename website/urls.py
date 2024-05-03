from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.HomeView.as_view(), name='home'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('profile/', views.profile, name='profile'),
    path('event/create/', views.EventCreate.as_view(), name='event-create'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update', views.EventUpdate.as_view(), name='event-update'),
    path('role/create/', views.RoleCreate.as_view(), name='role-create'),
    path('role/<uuid:pk>', views.RoleDetailView.as_view(), name='role-detail'),
    path('role/<uuid:pk>/update', views.RoleUpdate.as_view(), name='role-update'),

]

