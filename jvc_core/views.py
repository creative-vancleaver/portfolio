from django.shortcuts import render
from django.views import generic

from jvc_portfolio.models import Design, Development, Project, Software, Program
from jvc_portfolio.forms import ProjectForm

from jvc_resume.models import About, Employment, ProgrammingProjects, SupplimentalEducation, TechnicalSkills
from jvc_resume.forms import SupplimentalEducationForm
class HomeView(generic.TemplateView):
    template_name = 'core/index.html'
    
    def get_context_data(self, *args, **kwargs):
        
        print('request.user ', self.request.user)
        
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        projects = Project.objects.filter(project_type='DEV')
        # context['projects'] = projects
        
        abouts = About.objects.all()
        edu_list = SupplimentalEducation.objects.all()
        tech_skills_list = TechnicalSkills.objects.all()
        prog_proj_list = ProgrammingProjects.objects.all()
        employment_list = Employment.objects.all()
        
        project_form = ProjectForm()
        supp_edu_form = SupplimentalEducationForm()
        
        context = { 'projects': projects, 'abouts': abouts, 'edu_list': edu_list, 'tech_skills_list': tech_skills_list, 'prog_proj_list': prog_proj_list, 'employment_list': employment_list, 'project_form': project_form, 'supp_edu_form': supp_edu_form }
        
        return context

    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     des_proj_list = Project.objects.filter(project_type='DES')
    #     context['des_proj_list'] = des_proj_list

    #     return context
    