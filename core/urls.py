from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_application_view, name='create_application'),
    path('my-applications/', views.my_applications_view, name='my_applications'),
    path('admin-panel/', views.admin_panel_view, name='admin_panel'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]