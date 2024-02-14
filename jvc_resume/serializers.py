from rest_framework import serializers

from jvc_portfolio.models import Program
from .models import About, SupplimentalEducation, TechnicalSkills, ProgrammingProjects, Employment

class AboutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = About
        fields = ['text', 'header', 'image', 'updated_on']
        
class SupplimentalEducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SupplimentalEducation
        fields = ['name', 'type', 'year', 'pk']
        
class ProgrammingProjectsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProgrammingProjects
        fields = ['name', 'description', 'pk']
        
class EmploymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employment
        fields = ['name', 'start_date', 'end_date', 'job_title', 'pk']
        
class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Program
        fields = ['id', 'name']
        
class TechSkillSerializer(serializers.ModelSerializer):
    
    programs = ProgramSerializer(many=True)
    
    class Meta:
        model = TechnicalSkills
        fields = ['type', 'programs', 'pk']