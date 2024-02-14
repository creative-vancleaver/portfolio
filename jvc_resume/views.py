from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from .models import About, Employment, ProgrammingProjects, SupplimentalEducation, TechnicalSkills, Program
from .utils import redirect_to_self
from django import forms

from jvc_resume.forms import AboutForm, EmploymentForm, ProgrammingProjectForm, SupplimentalEducationForm, TechnicalSkillsForm
from .serializers import AboutSerializer, SupplimentalEducationSerializer, ProgrammingProjectsSerializer, EmploymentSerializer, TechSkillSerializer

# Create your views here.

# class ResumeListView(TemplateView):
#     template_name = 'resume/partials/resume_partial.html'
    
#     def get_context_data(self, *args, **kwargs):
#         context = super(ResumeListView, self).get_context_data(*args, **kwargs)

class AboutView(generic.TemplateView):
    template_name = 'resume/partials/resume_partial.html'
    form_classes = {'about': AboutForm,
                    'edu': SupplimentalEducationForm,
                    'skills': TechnicalSkillsForm,
                    'prog_proj': ProgrammingProjectForm,
                    'work_form': EmploymentForm,
                    }

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        about = About.objects.get(pk=1)
        context['about'] = about
        context['about_form'] = AboutForm(instance=about)

        edu_list = SupplimentalEducation.objects.all()
        context['edu_list'] = edu_list
        context['edu_form'] = SupplimentalEducationForm
        # context['update_edu_form'] = SupplimentalEducation(instance=)

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

# class AddAboutView(generic.CreateView):
#     model = About
#     # template_name = 'resume/add_about.html'
#     form_class = AboutForm
#     # success_url = reverse_lazy('about')

#     def get_success_url(self):
#         next = self.request.GET.get("next", None)

#         if next and next != '':
#             return next

#         return "/resume/about"

class PopulateForm(generic.View):
    
    def get(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            model = request.GET.get('model_name')
            id = request.GET.get('obj_id')
            # form_html = self.get_form_html(model, id)
            form_data = self.get_form_data(model, id)
            return JsonResponse({ 'success': True, 'form_data': form_data })
        return super().get(request, *args, **kwargs)
    
    def get_form_data(self, model, id):
        
        if model == 'SupplementalEducation':
            education = get_object_or_404(SupplimentalEducation, pk=id)
            # form = SupplimentalEducationForm(instance=education)
            form_data = {
                'name': education.name,
                'type': education.type,
                'pk': education.pk
            }
            return form_data
        elif model == 'TechSkills':
            print('tech skills')
            tech_skill = get_object_or_404(TechnicalSkills, pk=id)
            form_data = {
                'type': tech_skill.type,
                # 'programs': tech_skill.programs,
                'programs': [{ 'id': program.id, 'name': program.name } for program in tech_skill.programs.all()],
                'pk': tech_skill.pk
            }
            return form_data
        elif model == 'ProgrammingProject':
            print('programming project')
            project = get_object_or_404(ProgrammingProjects, pk=id)
            form_data = {
                'name': project.name,
                'description': project.description,
                'pk': project.pk
            }
            return form_data
        elif model == 'Employment':
            print('employment')
            employment = get_object_or_404(Employment, pk=id)
            form_data = {
                'name': employment.name,
                'job_title': employment.job_title,
                'start_date': employment.start_date,
                'end_date': employment.end_date,
                'pk': employment.pk
            }
            return form_data
        else:
            raise NotImplementedError(f'model { model } is not supported.')
        
        # return form.as_p()
            

class UpdateAboutView(generic.View):
    
    def post(self, request):
        
        about = About.objects.get(pk=1)
        
        form_about = request.POST.get('text')
        form_header = request.POST.get('header')
        form_image = request.FILES.get('image')
        
        about.text = form_about
        print('about form text ', form_about)
        about.header = form_header
        print('about.header ', about.header)
        if form_image:
            about.image = form_image

        if 'image-clear' in request.POST:
            about.image = None

        about.save()
        
        serializer = AboutSerializer(about, many=False)
        updated_about = serializer.data
        
        return JsonResponse({ 'succes': True, 'updated_about': updated_about })
         
# class AddEduView(generic.CreateView):
#     model = SupplimentalEducation
#     # template_name = 'resume/add_edu.html'
#     form_class = SupplimentalEducationForm
#     # success_url = reverse_lazy('about')

#     def get_success_url(self):
#         # next = self.request.GET.get("next", None)

#         # if next and next != '':
#         #     return next

#         # return "/resume/about"
#         return redirect_to_self(self)

class AddEduView(generic.View):
    
    def post(self, request):
        
        name = request.POST.get('name')
        type = request.POST.get('type')
        year = request.POST.get('year')
        
        education = SupplimentalEducation.objects.create(
            name = name,
            type = type,
            year = year
        )
        
        serializer = SupplimentalEducationSerializer(education, many=False)
        new_education = serializer.data
        
        return JsonResponse({ 'success': True, 'new_education': new_education })

class UpdateEduView(generic.View):
    
    def post(self, request):
        print(request)
        education = SupplimentalEducation.objects.get(pk=request.POST.get('pk'))
        print(education)
        name = request.POST.get('name')
        type = request.POST.get('type')
        
        education.name = name
        education.type = type
        
        if request.POST.get('year'):
            year = request.POST.get('year')
            education.year = year
            
        education.save()
        
        serializer = SupplimentalEducationSerializer(education, many=False)
        updated_education = serializer.data
        print(updated_education)
        
        return JsonResponse({ 'success': True, 'updated_education': updated_education })


class AddProgrammingProjectView(generic.View):
    
    def post(self, request):
        
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        programming_project = ProgrammingProjects.objects.create(
            name = name,
            description = description
        )
        
        serializer = ProgrammingProjectsSerializer(programming_project, many=False)
        new_prog_proj = serializer.data
        
        return JsonResponse({ 'success': True, 'new_prog_proj': new_prog_proj })

class UpdateProgrammingProject(generic.View):
    
    def post(self, request):
        programming_project = ProgrammingProjects.objects.get(pk=request.POST.get('pk'))
        print(programming_project)
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        programming_project.name = name
        programming_project.description = description
        
        programming_project.save()
        
        serializer = ProgrammingProjectsSerializer(programming_project, many=False)
        update_prog_proj = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_prog_proj': update_prog_proj })


class AddEmploymentView(generic.View):
    
    def post(self, request):
        
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        job_title = request.POST.get('job_title')
        
        employment = Employment.objects.create(
            name = name,
            start_date = start_date,
            job_title = job_title
        )
        
        if (request.POST.get('end_date')):
            end_date = request.POST.get('end_date')
            employment.end_date = end_date
            employment.save()
            
        serializer = EmploymentSerializer(employment, many=False)
        new_employment = serializer.data
        
        return JsonResponse({ 'success': True, 'new_employment': new_employment })

class UpdateEmployment(generic.View):
    
    def post(self, request):
        employment = Employment.objects.get(pk=request.POST.get('pk'))
        name = request.POST.get('name')
        job_title = request.POST.get('job_title')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        employment.name = name
        employment.job_title = job_title
        employment.start_date = start_date
        employment.end_date = end_date
        
        employment.save()
        
        serializer = EmploymentSerializer(employment, many=False)
        updated_employment = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_employment': updated_employment })


class AddTechSkillView(generic.View):
    
    def post(self, request):
        
        type = request.POST.get('type')
        skill_programs = request.POST.getlist('programs')
        print(skill_programs)
        
        tech_skill = TechnicalSkills.objects.create(
            type = type
        )
        
        # current_programs = Program.objects.all()
        # for program in current_programs:
        #     if(str(program.id) not in skill_programs):
        #         tech_skill
        
        if skill_programs:
            for program in skill_programs:
                tech_skill.programs.add(Program.objects.get(id=program))
                
        tech_skill.save()
        
        serializer = TechSkillSerializer(tech_skill, many=False)
        new_tech_skill = serializer.data
        print(new_tech_skill)
        
        return JsonResponse({ 'success': True, 'new_tech_skill': new_tech_skill })


class UpdateTechSkill(generic.View):
    
    def post(self, request):
        
        tech_skill = TechnicalSkills.objects.get(pk=request.POST.get('pk'))
        
        type = request.POST.get('type')
        skill_programs = request.POST.getlist('programs')
        
        current_programs = tech_skill.programs.all()
        for program in current_programs:
            if str(program.id) not in skill_programs:
                tech_skill.programs.remove(program)
                
        if skill_programs:
            for program in skill_programs:
                tech_skill.programs.add(Program.objects.get(id=program))
                
        tech_skill.type = type
        tech_skill.save()
        
        serializer = TechSkillSerializer(tech_skill, many=False)
        updated_tech_skill = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_tech_skill': updated_tech_skill })

# class AddTechSkillView(generic.CreateView):
#     model = TechnicalSkills
#     # template_name = 'resume/add_techskill.html'
#     form_class = TechnicalSkillsForm
#     # success_url = reverse_lazy('about')

#     def get_success_url(self):
#         return redirect_to_self(self)

# class AddProgrammingProjectView(generic.CreateView):
#     model = ProgrammingProjects
#     # template_name = 'resume/add_prog_proj.html'
#     form_class = ProgrammingProjectForm
#     # success_url = reverse_lazy('about')

#     def get_success_url(self):
#         return redirect_to_self(self)

# class AddEmploymentView(generic.CreateView):
#     model = Employment
#     # template_name = 'resume/add_employment.html'
#     form_class = EmploymentForm
#     # success_url = reverse_lazy('about')

#     def get_success_url(self):
#         return redirect_to_self(self)
