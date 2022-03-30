from django import forms
from .models import Project, Design, Development, Program, Software

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'image', 'project_type', 'about')

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),

            'project_type': forms.Select(attrs={
                # 'class': 'from-control',
                'id': 'projecttype',
                'type': 'hidden',
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'label': "",
            }),

            'about': forms.Textarea(attrs={
                'class': 'from-control',
                'label': '',
                'placeholder': 'Project Desicription',
                'style': 'width: 100%',
            }),

        }


# choices = Software.objects.all().values_list('name', 'name')
# software_list = []
# for item in choices:
#     software_list.append(item)

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ('title', 'project', 'image', 'description', 'software')

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