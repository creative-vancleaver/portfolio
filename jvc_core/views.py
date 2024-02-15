from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from decouple import config

from jvc_portfolio.models import Design, Development, Project, Software, Program
from jvc_portfolio.forms import ProjectForm, ProgramForm
from jvc_core.forms import ContactForm

from jvc_resume.models import About, Employment, ProgrammingProjects, SupplimentalEducation, TechnicalSkills
from jvc_resume.views import AboutView
from jvc_resume.forms import AboutForm, SupplimentalEducationForm, TechnicalSkillsForm, ProgrammingProjectForm, EmploymentForm

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
        
        program_form = ProgramForm()
        
        contact_form = ContactForm()
        
        context = { 'projects': projects, 'abouts': abouts, 'edu_list': edu_list, 'tech_skills_list': tech_skills_list, 'prog_proj_list': prog_proj_list, 'employment_list': employment_list, 'project_form': project_form, 'supp_edu_form': supp_edu_form, 'program_form': program_form, 'contact_form':  contact_form }
        
        resume = AboutView().get_context_data()
        context.update(resume)
        print(context)
        
        return context
    
def contact_form(request):
    
    print(config('ADMIN_EMAIL'))
    to_email = config('ADMIN_EMAIL')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print('message sent', sender_name, sender_email, subject, message)
            
            send_mail(
                subject,
                f'Name: { sender_name }\nEmail: { sender_email }\nMessage: { message }',
                to_email,
                [to_email],
                # config('ADMIN_EMAIL'),
                # [sender_email],
                # ['jacob@jacobvancleave.com'],
                fail_silently=False
            )
            
            return JsonResponse({ 'success': True })
        else:
            errors = dict(form.errors.items())
            return JsonResponse({ 'success': False, 'errors': errors })
        
    else:
        return JsonResponse({ 'success': False, 'errors': 'Invalid request method' })
        
    # def get(self, request, *args, **kwargs):
        
    #     # if request.is_ajax():
    #     if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpeRequest':
    #         model = request.GET.get('model_name')
    #         id = request.GET.get('obj_id')
    #         form_html = self.get_form_html(model, id)
    #         print('form_html', form_html)
    #         return JsonResponse({ 'form_html': form_html })
    #     return super().get(request, *args, **kwargs)
    
    # def get_form_html(self, model, id):
        
    #     if model == 'supplimentalEducation':
    #         education = get_object_or_404(SupplimentalEducation, pk=id)
    #         form = SupplimentalEducationForm(instance=education)
    #     elif model == 'technicalSkills':
    #         print('tech skills')
    #     else:
    #         raise NotImplementedError(f'Model {model} is not supported.')
        
    #     return form.as_p()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     des_proj_list = Project.objects.filter(project_type='DES')
    #     context['des_proj_list'] = des_proj_list

    #     return context
    