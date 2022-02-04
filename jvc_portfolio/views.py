from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import ListView, DetailView, CreateView

from .forms import DesignForm, ProjectForm

from .models import Project, Software, Design, Program, Development

# Create your views here.

class AddProjectView(CreateView):
    model = Project
    template_name = 'portfolio/add_project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('design_project_list')

class AddDesignView(CreateView):
    model = Design
    template_name = 'portfolio/add_design.html'
    form_class = DesignForm
    success_url = reverse_lazy('design_project_list')

class DesignProjectList(ListView):
    model = Design
    template_name = 'portfolio/design_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DesignProjectList, self).get_context_data(*args, **kwargs)
        des_proj_list = Project.objects.filter(project_type='DES')
        designs = Design.objects.all()

        # design_projects = Design.objects.filter(project=des_proj_list)
        # context['design_projects'] = design_projects

        context['des_proj_list'] = des_proj_list
        context['designs'] = designs

        return context

class DesignProjectView(DetailView):
    model = Design
    template_name = 'portfolio/design_project.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DesignProjectView, self).get_context_data(*args, **kwargs)
        # designs = Project.objects.filter(project_type='DES')
        # designs = Project.objects.filter(pk=self.kwargs['pk'])
        designs = Design.objects.filter(project=self.kwargs['pk'])
        context['designs'] = designs
        # project = Design.project
        # context['project'] = project
        

        return context

class DevelopmentProjectList(ListView):
    model = Project
    # dev_proj_list = Project.objects.filter(project_type='DEV')
    template_name = 'portfolio/development_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DevelopmentProjectList, self).get_context_data(*args, **kwargs)
        # dev_proj_list = Project.objects.filter(project_type='DEV')
        # dev_proj_list = Development.objects.all()
        # context['dev_proj_list'] = dev_proj_list

        des_proj_list = Project.objects.filter(project_type='DES')
        developments = Development.objects.all()

        context['des_proj_list'] = des_proj_list
        context['developments'] = developments

        return context

class DevelopmentProjectView(DetailView):
    model = Development
    template_name = 'portfolio/development_project.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DevelopmentProjectView, self).get_context_data(*args, **kwargs)
        # devs = Project.objects.filter(project_type='DEV')
        # devs = Development.objects.all()
        # context['devs'] = devs

        return context