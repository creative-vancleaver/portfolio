from django.urls import path

from . import views

urlpatterns = [

    path('add_project/', views.AddProjectView.as_view(), name='add_project'),

    path('design_projects/add_design/', views.AddDesignView.as_view(), name='add_design'),
    
    path('design_projects/', views.DesignProjectList.as_view(), name='design_project_list'),

    path('design_projects/<int:pk>/', views.DesignProjectView.as_view(), name='design_project_detail'),

    path('development_projects/', views.DevelopmentProjectList.as_view(), name='dev_project_list'),

    path('development_projects/<int:pk>', views.DevelopmentProjectView.as_view(), name='dev_project_detail'),
]