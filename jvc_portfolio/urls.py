from django.urls import path

from . import views

urlpatterns = [

    path('add_project/', views.AddProjectView.as_view(), name='add_project'),

    path('design_projects/<int:pk>/add_design/', views.AddDesignView.as_view(), name='add_design'),
    
    path('design_projects/', views.DesignProjectList.as_view(), name='design_project_list'),

    path('design_projects/<int:pk>/', views.DesignProjectView.as_view(), name='design_project_detail'),

    path('development_projects/<int:pk>/add_development/', views.AddDevelopmentView.as_view(), name='add_dev'),

    path('development_projects/', views.DevelopmentProjectList.as_view(), name='dev_project_list'),

    path('development_projects/<int:pk>/forum/', views.ForumView.as_view(), name='forum'),

    path('development_projects/<int:pk>/cell_label/', views.CellLabelView.as_view(), name='cell_label'),

    # path('development_projects/<int:pk>/forum/', views.ForumView.as_view(), name='forum'),
]