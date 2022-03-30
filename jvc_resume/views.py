from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import About, Employment, ProgrammingProjects, SupplimentalEducation, TechnicalSkills
from .utils import redirect_to_self
from django import forms
from jvc_resume.forms import AboutForm, EmploymentForm, ProgrammingProjectForm, SupplimentalEducationForm, TechnicalSkillsForm

# Create your views here.

class AboutView(generic.TemplateView):
    template_name = 'resume/about.html'
    form_classes = {'about': AboutForm,
                    'edu': SupplimentalEducationForm,
                    'skills': TechnicalSkillsForm,
                    'prog_proj': ProgrammingProjectForm,
                    'work_form': EmploymentForm,
                    }

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        abouts = About.objects.all()
        context['abouts'] = abouts
        context['about_form'] = AboutForm

        edu_list = SupplimentalEducation.objects.all()
        context['edu_list'] = edu_list
        context['edu_form'] = SupplimentalEducationForm

        tech_skill_list = TechnicalSkills.objects.all()
        context['tech_skill_list'] = tech_skill_list
        context['skills_form'] = TechnicalSkillsForm

        prog_proj_list = ProgrammingProjects.objects.all()
        context['prog_proj_list'] = prog_proj_list
        context['prog_proj_form'] = ProgrammingProjectForm

        employment_list = Employment.objects.all()
        context['employment_list'] = employment_list
        context['work_form'] = EmploymentForm

        return context

class AddAboutView(generic.CreateView):
    model = About
    # template_name = 'resume/add_about.html'
    form_class = AboutForm
    # success_url = reverse_lazy('about')

    def get_success_url(self):
        next = self.request.GET.get("next", None)

        if next and next != '':
            return next

        return "/resume/about"

class AddEduView(generic.CreateView):
    model = SupplimentalEducation
    # template_name = 'resume/add_edu.html'
    form_class = SupplimentalEducationForm
    # success_url = reverse_lazy('about')

    def get_success_url(self):
        # next = self.request.GET.get("next", None)

        # if next and next != '':
        #     return next

        # return "/resume/about"
        return redirect_to_self(self)


class AddTechSkillView(generic.CreateView):
    model = TechnicalSkills
    # template_name = 'resume/add_techskill.html'
    form_class = TechnicalSkillsForm
    # success_url = reverse_lazy('about')

    def get_success_url(self):
        return redirect_to_self(self)

class AddProgrammingProjectView(generic.CreateView):
    model = ProgrammingProjects
    # template_name = 'resume/add_prog_proj.html'
    form_class = ProgrammingProjectForm
    # success_url = reverse_lazy('about')

    def get_success_url(self):
        return redirect_to_self(self)

class AddEmploymentView(generic.CreateView):
    model = Employment
    # template_name = 'resume/add_employment.html'
    form_class = EmploymentForm
    # success_url = reverse_lazy('about')

    def get_success_url(self):
        return redirect_to_self(self)
