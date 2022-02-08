from django.urls import path

from . import views

urlpatterns = [
    
    path('about/', views.AboutView.as_view(), name='about'),

    path('add_about/', views.AddAboutView.as_view(), name='add_about'),

    path('add_edu/', views.AddEduView.as_view(), name='add_edu'),

    path('add_techskill/', views.AddTechSkillView.as_view(), name='add_techskill'),

    path('add_programming_project/', views.AddProgrammingProjectView.as_view(), name='add_programming_project'),

    path('add_employment/', views.AddEmploymentView.as_view(), name='add_employment'),
]