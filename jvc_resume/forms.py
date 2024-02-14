from django import forms 
from django.forms import widgets
from django.core.exceptions import ValidationError

from datetime import datetime

from jvc_resume.models import About, SupplimentalEducation, TechnicalSkills, ProgrammingProjects, Employment, Program


current_year = datetime .now().year
YEARS = [(year, str(year)) for year in range(current_year, current_year - 10, -1)]

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('image', 'header', 'text')
        
        widgets = {
            
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control mb-2',
            }),
            
            'header': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            }),
            
            'text': forms.Textarea(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Bio Text',
                'style': 'width: 100%',
            }),
        }
        
class YearField(forms.IntegerField):
    
    def to_python(self, value):
        try:
            return super().to_python(value)
        except forms.ValidationError:
            return None
        
    def validate(self, value):
        super().validate(value)
        if value is not None and (value < 1000 or value > 9999):
            raise ValidationError('Enter a valid year.')

class SupplimentalEducationForm(forms.ModelForm):
    
    class Meta:
        model = SupplimentalEducation
        fields = ('name', 'type', 'year')
        labels = {
            'name': 'Name',
        }
        
        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            }),
            
            'type': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            }),
            
            'year': forms.Select(choices=YEARS, attrs={
                'class': 'form-control mb-2',
            }),
        }
        
    # year = YearField(label='Year')
    
# class UpdateSupplimentalEducationForm(forms.ModelForm):
    
#     class Meta:
#         model = SupplimentalEducation
#         fields =

class TechnicalSkillsForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkills
        fields = ('type', 'programs')
        
        widgets = {
            
            'type': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            
            # 'programs': forms.CheckboxSelectMultiple(attrs={
            #     'class': 'form-control',
            # }),
        }
        
    programs = forms.ModelMultipleChoiceField(
        queryset = Program.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

class ProgrammingProjectForm(forms.ModelForm):
    class Meta:
        model = ProgrammingProjects
        fields = ('name', 'description')
        
        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100% mb-2',
            }),
        }

class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = ('name', 'job_title')
        
        labels = {
            'name': 'Company Name',
            'job_title': 'Job Title',
        }

        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            }),
            
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            # 'start_date': forms.DateInput(attrs={
            #     'class': 'form-control',
            #     'type': 'date'
            # }),
            
            # 'end_date': forms.DateInput(attrs={
            #     'class': 'form-control',
            #     'type': 'date'
            # })
            
        }