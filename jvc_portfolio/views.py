from curses.ascii import HT
from multiprocessing.context import BaseContext
from django.forms import model_to_dict
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from urllib.parse import quote

from django.contrib.auth.decorators import login_required

from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import UpdateView

from .forms import DesignForm, DevelopmentForm, ProjectForm, ProjectBriefForm, ProjectImgIForm, ProjectProcessIForm, ProjectImgIIForm, ProjectProcessIIForm, ProjectImgIIIForm, ProjectImgIVForm, ProjectProcessIIIForm, ProjectImgVForm, ProjectProcessIVForm, ProjectImgVIForm, ProjectProcessVForm, ProjectImgVIIForm, ProjectProcessVIForm, ProjectResponsiveImgIForm

from .models import Project, Software, Design, Program, Development

from .serializers import ProjectSerializer, ProjectBriefSerializer, ImageISerializer, ProcessISerializer, ImageIISerializer, ProcessIISerializer, ImageIIISerializer, ImageIVSerializer, ProcessIIISerializer, ImageVSerializer, ProcessIVSerializer, ImageVISerializer, ProcessVSerializer, ImageVIISerializer, ProcessVISerializer, ResponsiveISerializer, ProgramSerializer

# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/partials/project_list_partial.html'
    context_object_name = 'projects'
    
    def get_context_data(self, *args, **kwargs):
        print('get context data')
        context = super().get_context_data(*args, **kwargs)
        # projects = Project.objects.all()
        # context['projects'] = projects
        # print('projects = ', projects)
        return context
class ProjectDetailView(DetailView):
    print('projecct detail view')
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    # def get_object(self):
    #     return get_object_or_404(Project, id=self.kwargs['pk'])
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
        # project = Project.objects.filter(pk=self.kwargs['pk'])
        # context['project'] = project
        # print('project = ', ProjectSerializer(project, many=False))
        # print('project = ', context['project'])
        project = self.get_object()
        update_project_form = ProjectForm(instance=project)
        project_brief_form = ProjectBriefForm(instance=project)
        project_img_i_form = ProjectImgIForm(instance=project)
        project_process_i_form = ProjectProcessIForm(instance=project)
        project_img_ii_form = ProjectImgIIForm(instance=project)
        project_process_ii_form = ProjectProcessIIForm(instance=project)
        project_img_iii_form = ProjectImgIIIForm(instance=project)
        project_img_iv_form = ProjectImgIVForm(instance=project)
        project_process_iii_form = ProjectProcessIIIForm(instance=project)
        project_img_v_form = ProjectImgVForm(instance=project)
        project_process_iv_form = ProjectProcessIVForm(instance=project)
        project_img_vi_form = ProjectImgVIForm(instance=project)
        project_process_v_form = ProjectProcessVForm(instance=project)
        project_img_vii_form = ProjectImgVIIForm(instance=project)
        project_process_vi_form = ProjectProcessVIForm(instance=project)
        project_responsive_i_form = ProjectResponsiveImgIForm(instance=project)
        context.update({
            'project': project,
            'project_brief_form': project_brief_form,
            'project_img_i_form': project_img_i_form,
            'project_process_i_form': project_process_i_form,
            'project_img_ii_form': project_img_ii_form,
            'project_process_ii_form': project_process_ii_form,
            'project_img_iii_form': project_img_iii_form,
            'project_img_iv_form': project_img_iv_form,
            'project_process_iii_form': project_process_iii_form,
            'project_img_v_form': project_img_v_form,
            'project_process_iv_form': project_process_iv_form,
            'project_img_vi_form': project_img_vi_form,
            'project_process_v_form': project_process_v_form,
            'project_img_vii_form': project_img_vii_form,
            'project_process_vi_form': project_process_vi_form,
            'project_responsive_i_form': project_responsive_i_form,
        })
        
        print(context)
        
        return context
# class AddProjectView(CreateView):
#     model = Project
#     template_name = 'portfolio/partials/add_project.html'
#     form_class = ProjectForm
#     # success_url = reverse_lazy('dev_project_list')

#     def get_success_url(self):
#         next = self.request.GET.get("next", None)

#         if next and next != '':
#             return next

#         return "/home"
    
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         print(form)
#         return form

class AddProjectView(generic.View):
    
    def post(self, request, *args, **kwargs):
        print('Greetings from AddProjectView post method')
        print('data = ', request.POST, request.FILES)
        
        project_title = request.POST.get('title')
        project_name = request.POST.get('name')
        project_type = request.POST.get('project_type')
        project_about = request.POST.get('about')
        
        project_image = request.FILES.get('image')
        
        project = Project.objects.create(
            title = project_title,
            name = project_name,
            project_type = project_type,
            about = project_about,
            image = project_image
        )
        
        print(project)
        project.save()
        
        # project.image = quote(project.image.url, safe=':/')
        
        serializer = ProjectSerializer(project, many=False)
        new_project = serializer.data
        print('new_project ', new_project)
        
        return JsonResponse({ 'success': True, 'new_project': new_project })
    
    
class UpdateProjectBriefView(generic.View):
    
    def post(self, request, *args, **kwargs):
        print('Greetings from UpdateProjectBreifView')
        print('data = ', request.POST)
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        
        project_year = request.POST.get('year')
        project_programs = request.POST.getlist('programs')
        print(project_programs)
        project_subtitle = request.POST.get('sub_title')
        project_brief = request.POST.get('brief')
        
        project.year = project_year
        
        current_programs = project.programs.all()
        for program in current_programs:
            if str(program.id) not in project_programs:
                project.programs.remove(program)
                
        if project_programs:
             # project.programs.set(project_programs)
             for program in project_programs:
                print(program)
                project.programs.add(Program.objects.get(id=program))
        project.sub_title = project_subtitle
        project.brief = project_brief
        
        project.save()
        
        serializer = ProjectBriefSerializer(project, many=False)
        updated_project = serializer.data
        print('updated_project ', updated_project)
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
    
    
class UpdateImageI(generic.View):
    
    def post(self, request, *args, **kwargs):
        print('Project Image I')
        print('data = ', request.POST, request.FILES)
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        fullpage_imgI = request.FILES.get('fullpage_imgI')
        project.fullpage_imgI = fullpage_imgI
        project.save()
        
        serializer = ImageISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
    
class UpdateProcessI(generic.View):
    
    def post(self, request, *args, **kwargs):
        print('Project Process I')
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        banner_textI = request.POST.get('banner_textI')
        processI = request.POST.get('processI')
        
        project.banner_textI = banner_textI
        project.processI = processI
        project.save()
        
        serializer = ProcessISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
    
class UpdateImageII(generic.View):
    
    def post(self, request, *args, **kwargs):
        print('Project Image II')
        print('data = ', request.POST, request.FILES)
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        fullpage_imgII = request.FILES.get('fullpage_imgII')
        project.fullpage_imgII = fullpage_imgII
        project.save()
        
        serializer = ImageIISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
    
class UpdateProcessII(generic.View):
    
    def post(self, request):
        print('Process II')
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        processII = request.POST.get('processII')
        
        project.processII = processII
        project.save()
        
        serializer = ProcessIISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })

class UpdateImageIII(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        fullpage_imgIII = request.FILES.get('fullpage_imgIII')
        project.fullpage_imgIII = fullpage_imgIII
        project.save()
        
        serializer = ImageIIISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
    
class UpdateImageIV(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        fullpage_imgIV = request.FILES.get('fullpage_imgIV')
        project.fullpage_imgIV = fullpage_imgIV
        project.save()
        
        serializer = ImageIVSerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })

class UpdateProcessIII(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        processIII = request.POST.get('processIII')
        processIV = request.POST.get('processIV')
        
        project.processIII =processIII
        project.processIV = processIV
        project.save()
        
        serializer = ProcessIIISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })

class UpdateImageV(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        fullpage_imgV = request.FILES.get('fullpage_imgV')
        project.fullpage_imgV = fullpage_imgV
        project.save()
        
        serializer = ImageVSerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })

class UpdateProcessIV(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        processV = request.POST.get('processV')
        project.processV = processV
        project.save()
        
        print(project.processIV)
        
        serializer = ProcessIVSerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
        
class UpdateImageVI(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        imageVI = request.FILES.get('fullpage_imgVI')
        project.fullpage_imgVI = imageVI
        project.save()
        
        seraizlier = ImageVISerializer(project, many=False)
        updated_project = seraizlier.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })

class UpdateProcessV(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        processVI = request.POST.get('processVI')
        processVII = request.POST.get('processVII')
        project.processVI = processVI
        project.processVII = processVII
        project.save()
        
        serializer = ProcessVSerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
    
class UpdateImageVII(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        imageVII = request.FILES.get('fullpage_imgVII')
        project.fullpage_imgVII = imageVII
        project.save()
        
        serializer = ImageVIISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })
    
class UpdateProcessVI(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        processVIII = request.POST.get('processVIII')
        processIX = request.POST.get('processIX')
        
        project.processVIII = processVIII
        project.processIX = processIX
        project.save()
        
        serializer = ProcessVISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })

class UpdateResponsiveI(generic.View):
    
    def post(self, request):
        
        project = Project.objects.get(pk=request.POST.get('project_id'))
        responsiveI = request.FILES.get('responsive_imgI')
        responsiveII = request.FILES.get('responsive_imgII')
        responsiveIII = request.FILES.get('responsive_imgIII')
        bannerII = request.POST.get('banner_textII')
        
        project.responsive_imgI = responsiveI
        project.responsive_imgII = responsiveII
        project.responsive_imgIII = responsiveIII
        project.banner_textII = bannerII
        project.save()
        
        serializer = ResponsiveISerializer(project, many=False)
        updated_project = serializer.data
        
        return JsonResponse({ 'success': True, 'updated_project': updated_project })

def add_project(request):
    print('greetings from add_project function view')
    
    return JsonResponse()

class UpdateProjectView(generic.View):
    
    def post(self, request, *args, **kwargs):
        
        project = Project.objects.get(pk=self.kwargs['pk'])
        # project = get_object_or_404(Project, pk=self.kwargs['pk'])
        project_dict = model_to_dict(project)
        
        update_project_form = ProjectForm(request.POST, request.FILES, initial=project_dict, instance=project)
        
        print('has changed ', update_project_form.has_changed())
        
        if update_project_form.has_changed():
            
            if update_project_form.is_valid():
                
                changed_fields = update_project_form.changed_data
                print('changed data ', changed_fields)
                
                for field_name in changed_fields:
                    
                    field_value = update_project_form.cleaned_data[field_name]
                    
                    if hasattr(project, field_name) and isinstance(getattr(project, field_name), models.Manager):
                        getattr(project, field_name).set(field_value)
                    else:
                        setattr(project, field_name, field_value)
                    # if field_value != project_dict[field_name] and field_value is not None:
                    #     if isinstance(field_value, InMemoryUploadedFile) and field_value.size == 0:
                    #         continue
                        
                    #     if has
                    # # if field_value != project.dict[field_name]:
                    # # new_value = update_project_form.cleaned_data.get(field_name)
                    # # project.field_name = new_value
                    #     setattr(project, field_name, field_value)
                    
                project.save()
        
                return JsonResponse({ 'success': True })
            
            else:
                errors = update_project_form.errors
                return JsonResponse({ 'success': False, 'errors': errors })
        else:
            
            return JsonResponse({ 'message': 'No changes were made.' })
        
        
class AddProgram(generic.View):
    
    def post(self, request):
        program_name = request.POST.get('name')
        
        program = Program.objects.create(name=program_name)
        
        serializer = ProgramSerializer(program, many=False)
        new_program = serializer.data
        
        return JsonResponse({ 'success': True, 'new_program': new_program })



# class UpdateProjectView(UpdateView):
#     model = Project
#     form_class = ProjectForm()
#     # template_name = 'portfolio/modals/add_project_modal.html'
    
#     print('Update Project View')
    
#     def get(self, request, *args, **kwargs):
#         print('greetigns from updateProject GET method')
#         print('self === ', self)
        
#         return JsonResponse()
    
#     def render_to_response(self, context, **response_kwargs):
#         if self.request.is_ajax():
#             return render(self.request, 'portfolio/modals/udpate_project_modal.html', context)
#         return super().render_to_response(context, **response_kwargs)
            

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
    form_class = ProjectForm
    template_name = 'portfolio/design_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DesignProjectList, self).get_context_data(*args, **kwargs)
        des_proj_list = Project.objects.filter(project_type='DES')
        designs = Design.objects.all()
        context['des_proj_list'] = des_proj_list
        context['designs'] = designs
        context['form'] = ProjectForm

        return context
    

    

class DesignProjectView(DetailView):
    model = Project
    form_class = DesignForm
    template_name = 'portfolio/design_project.html'

    def get_context_data(self, *args, **kwargs):
        print('entering DESIGNPROJECT get_context_data')
        print(kwargs)
        context = super(DesignProjectView, self).get_context_data(*args, **kwargs)
        designs = Design.objects.filter(project__pk=self.kwargs['pk'])
        context['designs'] = designs
        print(designs)
        context['form'] = DesignForm

        return context

class DevelopmentProjectList(ListView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/development_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DevelopmentProjectList, self).get_context_data(*args, **kwargs)
        dev_proj_list = Project.objects.filter(project_type='DEV')

        # for proj in dev_proj_list:
        #     proj_pk = proj.pk
        #     print(proj_pk)
        #     context['proj_pk'] = proj_pk

        developments = Development.objects.all()
        # dev_pk = Development.objects.filter(project__pk=self)
        # context['dev_pk'] = dev_pk
        print(dev_proj_list)
        context['dev_proj_list'] = dev_proj_list
        context['developments'] = developments
        context['form'] = ProjectForm

        print(context)

        return context

    def get_success_url(self):
        return reverse('dev_proj_list')

# class DevelopmentProjectView(DetailView):
#     model = Project
#     form_class = DevelopmentForm

#     template_name = 'portfolio/development_project.html'

#     def get_context_data(self, *args, **kwargs):
#         print('entering get_context_data')
#         print(kwargs)
#         context = super(DevelopmentProjectView, self).get_context_data(*args, **kwargs)
#         developments = Development.objects.filter(project__pk=self.kwargs['pk'])
#         context['developments'] = developments
#         context['form'] = DevelopmentForm

#         print(context)

#         return context

class BaseContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(BaseContextMixin, self).get_context_data(**kwargs)
        developments = Development.objects.filter(project__pk=kwargs['pk'])
        context['developments'] = developments

        return context

class ForumView(TemplateView, BaseContextMixin):
    template_name = "portfolio/forum.html"

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        # context['pk'] = Development.objects.get(kwargs['pk'])
        return context

class CellLabelView(TemplateView, BaseContextMixin):
    template_name = "portfolio/cell_label.html"

    def get_context_data(self, **kwargs):
        context = super(CellLabelView, self).get_context_data(**kwargs)
        return context



# class ForumView(TemplateView):
#     template_name = "forum.html"
