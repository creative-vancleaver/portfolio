from django.urls import path

from . import views

urlpatterns = [
    
    path('project/<str:project_name>/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    
    path('project_list/', views.ProjectListView.as_view(), name='project_list'),

    path('add_project/', views.AddProjectView.as_view(), name='add_project'),
    # path('add_project/', views.add_project, name='add_project'),
    
    path('update_brief/', views.UpdateProjectBriefView.as_view(), name='update_brief'),
    
    path('update_imageI/', views.UpdateImageI.as_view(), name='update_imageI'),
    path('update_processI/', views.UpdateProcessI.as_view(), name='update_processI'),
    path('update_imageII/', views.UpdateImageII.as_view(), name='update_imageII'),
    path('update_processII/', views.UpdateProcessII.as_view(), name='update_processII'),
    path('update_imageIII/', views.UpdateImageIII.as_view(), name='update_imageIII'),
    path('update_imageIV/', views.UpdateImageIV.as_view(), name='update_imageIV'),
    path('update_processIII/', views.UpdateProcessIII.as_view(), name='update_processIII'),
    path('update_imageV/', views.UpdateImageV.as_view(), name='update_imageV'),
    path('update_processIV/', views.UpdateProcessIV.as_view(), name='update_projectIV'),
    path('update_imageVI/', views.UpdateImageVI.as_view(), name='update_imageVI'),
    path('update_processV/', views.UpdateProcessV.as_view(), name='update_processV'),
    path('update_imageVII/', views.UpdateImageVII.as_view(), name='update_imageVII'),
    path('update_processVI/', views.UpdateProcessVI.as_view(), name='update_processVI'),
    path('update_responsiveI/', views.UpdateResponsiveI.as_view(), name='update_responsiveI'),
    
    path('add_program/', views.AddProgram.as_view(), name='add_program'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('update_project/<int:pk>/', views.UpdateProjectView.as_view(), name='update_project'),

   
   
   
    path('design_projects/<int:pk>/add_design/', views.AddDesignView.as_view(), name='add_design'),
    
    path('design_projects/', views.DesignProjectList.as_view(), name='design_project_list'),

    # path('design_projects/<int:pk>/', views.DesignProjectView.as_view(), name='design_project_detail'),

    path('development_projects/<int:pk>/add_development/', views.AddDevelopmentView.as_view(), name='add_dev'),

    path('development_projects/', views.DevelopmentProjectList.as_view(), name='dev_project_list'),

    path('development_projects/<int:pk>/forum/', views.ForumView.as_view(), name='forum'),

    path('development_projects/<int:pk>/cell_label/', views.CellLabelView.as_view(), name='cell_label'),
    
    path('development_projects/<int:pk>/1k_words/', views.ForumView.as_view(), name='1k_words'),

    # path('development_projects/<int:pk>/forum/', views.ForumView.as_view(), name='forum'),
]