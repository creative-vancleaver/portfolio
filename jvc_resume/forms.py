from django import forms 
from django.forms import widgets
from jvc_resume.models import About, SupplimentalEducation, TechnicalSkills, ProgrammingProjects, Employment, Program

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('text',)

class SupplimentalEducationForm(forms.ModelForm):
    class Meta:
        model = SupplimentalEducation
        fields = ('name', 'type', 'year')

class TechnicalSkillsForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkills
        fields = ('type', 'programs')

        programs = forms.ModelMultipleChoiceField(
            queryset = Program.objects.all(),
            widget = forms.CheckboxSelectMultiple
        )

class ProgrammingProjectForm(forms.ModelForm):
    class Meta:
        model = ProgrammingProjects
        fields = ('name', 'description')

class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = ('name', 'job_title', 'start_date', 'end_date')

        widgets = {
            'start_date': widgets.DateInput(attrs={
                'type': 'date'
            }),
            'end_date': widgets.DateInput(attrs={
                'type': 'date'
            })
        }