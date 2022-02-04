from django.shortcuts import render
from django.views import generic

from jvc_portfolio.models import Design, Development, Project, Software, Program

class HomeView(generic.TemplateView):
    template_name = 'core/index.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     des_proj_list = Project.objects.filter(project_type='DES')
    #     context['des_proj_list'] = des_proj_list

    #     return context
    