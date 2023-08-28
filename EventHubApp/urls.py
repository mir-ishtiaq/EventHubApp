from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     # path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_login, name='login'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('create_event/', views.create_event, name='create_event'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),



]