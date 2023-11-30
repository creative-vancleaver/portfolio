from django import forms
from .models import Project, Design, Development, Program, Software

from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


# class CustomFileInput(forms.ClearableFileInput):
#     def render(self, name, value, attrs=None, renderer=None):
#         template = super().render(name, value, attrs, renderer)
#         current_image = ''
#         if value and hasattr(value, 'url'):
#             current_image = f'Current Image: { value.url }'
#         return f'{ template }<p>{ current_image }</p>'

class CustomFileInput(forms.FileInput):
    
    def __init__(self, attrs={}):
        super(CustomFileInput, self).__init__(attrs)
        
    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, 'url'):
            output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' % (_('Currently:'), value.url, value, _('Change:')))
        output.append(super(CustomFileInput, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'name', 'image', 'project_type', 'about')

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),

            'project_type': forms.Select(attrs={
                'class': 'from-control',
                'id': 'projecttype',
                'type': 'hidden',
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'image',
            }),

            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'label': '',
                'placeholder': 'Project Desicription',
                'style': 'width: 100%',
            }),

        }


class ProjectBriefForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('id', 'year', 'programs', 'sub_title', 'brief')
        
        widgets = {
            
            'id': forms.HiddenInput(attrs={
                'class': 'form-control',
                'label': 'id',
                'type': 'hidden',
            }),
            
            'sub_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sub Title',
            }),
            
            'year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Year',
            }),
            
            'brief': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Brief',
                'style': 'width: 100%',
            }),    
                    
        }
        
    programs = forms.ModelMultipleChoiceField(
        queryset = Program.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )
    
class ProjectImgIForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('fullpage_imgI', )
        
        widgets = {
            
            'fullpage_imgI': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Full Page Image',
            })
        }
        
class ProjectProcessIForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('banner_textI', 'processI')
        
        widgets = {
            
            'banner_textI': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Banner Text',
                'style': 'width: 100%',
            }),
            
            'processI': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Process',
            }),
        }
        
class ProjectImgIIForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('fullpage_imgII',)
        
        widgets = {
            
            'fullpage_imgII': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Full Page Image'
            }),
        }
        
class ProjectProcessIIForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('processII',)
        
        widgets = {
            
            'processII': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process II',
                'style': 'width: 100%',
            }),
        }
 
class ProjectImgIIIForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('fullpage_imgIII',)
        
        widgets = {
            
            'fullpage_imgIII': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Full Page Image III',
            }),
        }
        
class ProjectImgIVForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('fullpage_imgIV',)
        
        widgets = {
            
            'fullpage_imgIV': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Full Page Image IV',
            })
        }
        
class ProjectProcessIIIForm(forms.ModelForm): 
    
    class Meta:
        model = Project
        fields = ('processIII', 'processIV')
        
        widgets = {
            
            'processIII': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process III',
                'style': 'width: 100%',
            }),
            
            'processIV': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process IV',
                'style': 'width: 100%',
            })
        }
    
class ProjectImgVForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('fullpage_imgV',)
        
        widgets = {
            'fullpage_imgV': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Full Page Image V'
            })
        }
        
class ProjectProcessIVForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('processV',)
        
        widgets = {
            'processV': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process V',
                'style': 'width: 100%',
            })
        }
        
class ProjectImgVIForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('fullpage_imgVI',)
        
        widgets = {
            'fullpage_imgVI': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'full Page Image VI',
            })
        }
        
class ProjectProcessVForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('processVI', 'processVII')
        
        widgets = {
            'processVI': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process VI',
                'style': 'wdith: 100%',
            }),
            'processVII': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process VII',
                'style': 'width 100%',
            })
        }
        
class ProjectImgVIIForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('fullpage_imgVII',)
        
        widgets = {
            'fullpage_imgVII': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Full Page Image VII'
            })
        }
        
class ProjectProcessVIForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('processVIII', 'processIX')
        
        widgets = {
            'processVIII': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process VIII',
                'style': 'width: 100%',
            }),
            'processIX': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Process IX',
                'style': 'widgth: 100%',
            })
        }
        
class ProjectResponsiveImgIForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('responsive_imgI', 'responsive_imgII', 'banner_textII', 'responsive_imgIII')
        
        widgets = {
            'responsive_imgI': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Responsive Img I',
            }),
            'responsive_imgII': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Responsive Img II',
            }),
            'banner_textII': forms.Textarea(attrs={
                'class': 'form-control',
                'label': 'Banner Text II',
                'style': 'width: 100%',
            }),
            'responsive_imgIII': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Responsive Img III',
            }),
        }

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ('title', 'project', 'banner_img', 'brief', 'software')

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title',
            }),
            
            'project': forms.Select(attrs={
                'class': 'form-control',
                'id': 'project',
                'type': 'hidden',
            }),

            'banner_img': forms.FileInput(attrs={
                'class': 'form-control',
                'label': "",
            }),

            'brief': forms.Textarea(attrs={
                'class': 'form-control',
                'label': '',
                'placeholder': 'Brief',
                'style': 'width: 100%',
            }),

            'software': forms.Select(attrs={
                'class': 'form-control',
                # 'style': 'display: inline',
            }),
        }

    software = forms.ModelMultipleChoiceField(
        queryset = Software.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

class DevelopmentForm(forms.ModelForm):
    class Meta:
        model = Development
        fields = ('title', 'project', 'image', 'description', 'programs')

    programs = forms.ModelMultipleChoiceField(
        queryset = Program.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )