from django.urls import path

from .import views

urlpatterns = [
    
    path('user_login/', views.UserLoginView.as_view(), name='login'),
    
    path('user_logout/', views.UserLogout.as_view(), name='logout'),
    
]