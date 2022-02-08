from curses.ascii import HT
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


from django.views import generic
from django.views.generic import ListView, DetailView, CreateView

from .forms import DesignForm, DevelopmentForm, ProjectForm

from .models import Project, Software, Design, Program, Development

# Create your views here.

class AddProjectView(CreateView):
    model = Project
    template_name = 'portfolio/add_project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('home')

class AddDesignView(CreateView):
    model = Design
    template_name = 'portfolio/add_design.html'
    form_class = DesignForm
    # success_url = reverse_lazy('design_project_list')

    def get_success_url(self):
        project_pk = self.kwargs['pk']
        return reverse('design_project_detail', kwargs={'pk': project_pk})

class AddDevelopmentView(CreateView):
    model = Development
    template_name = 'portfolio/add_development.html'
    form_class = DevelopmentForm
    # success_url = reverse_lazy('dev_project_list')

    def get_success_url(self):
        project_pk = self.kwargs['pk']
        return reverse('dev_project_detail', kwargs={'pk': project_pk})

class DesignProjectList(ListView):
    model = Project
    template_name = 'portfolio/design_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DesignProjectList, self).get_context_data(*args, **kwargs)
        des_proj_list = Project.objects.filter(project_type='DES')
        designs = Design.objects.all()
        context['des_proj_list'] = des_proj_list
        context['designs'] = designs

        return context

class DesignProjectView(DetailView):
    model = Project
    template_name = 'portfolio/design_project.html'

    def get_context_data(self, *args, **kwargs):
        print('entering DESIGNPROJECT get_context_data')
        print(kwargs)
        context = super(DesignProjectView, self).get_context_data(*args, **kwargs)
        designs = Design.objects.filter(project__pk=self.kwargs['pk'])
        context['designs'] = designs

        return context

class DevelopmentProjectList(ListView):
    model = Project
    template_name = 'portfolio/development_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DevelopmentProjectList, self).get_context_data(*args, **kwargs)
        dev_proj_list = Project.objects.filter(project_type='DEV')
        developments = Development.objects.all()
        context['dev_proj_list'] = dev_proj_list
        context['developments'] = developments

        return context

class DevelopmentProjectView(DetailView):
    model = Project
    template_name = 'portfolio/development_project.html'

    def get_context_data(self, *args, **kwargs):
        print('entering get_context_data')
        print(kwargs)
        context = super(DevelopmentProjectView, self).get_context_data(*args, **kwargs)
        developments = Development.objects.filter(project__pk=self.kwargs['pk'])
        context['developments'] = developments

        print(context)

        return context

