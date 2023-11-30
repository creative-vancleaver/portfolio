from rest_framework import serializers
from .models import Project, Program

class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Program
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'
        
class ProjectBriefSerializer(serializers.ModelSerializer):
    
    programs = ProgramSerializer(many=True)
    
    class Meta:
        model = Project
        fields = ['year', 'programs', 'sub_title', 'brief']
        
class ImageISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['fullpage_imgI',]
        
class ProcessISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['banner_textI', 'processI']
        
class ImageIISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['fullpage_imgII',]
        
class ProcessIISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['processII',]
        
class ImageIIISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['fullpage_imgIII',]
        
class ImageIVSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['fullpage_imgIV',]
        
class ProcessIIISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['processIII', 'processIV']
        
class ImageVSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['fullpage_imgV',]
        
class ProcessIVSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['processV',]
        
class ImageVISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['fullpage_imgVI',]
        
class ProcessVSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['processVI', 'processVII']
        
class ImageVIISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['fullpage_imgVII',]
        
class ProcessVISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['processVIII', 'processIX']
        
class ResponsiveISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['responsive_imgI', 'responsive_imgII', 'responsive_imgIII', 'banner_textII']