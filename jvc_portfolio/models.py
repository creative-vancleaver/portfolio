import os
from statistics import mode
from unittest import mock
from django.db import models

# Create your models here.

class Software(models.Model):

    name = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Software'

    def __str__(self):
        return self.name
    
class Program(models.Model):

    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

def project_path(instance, filename):
    return '/'.join(['images/proj', str(instance.name), filename])

class Project(models.Model):

    DESIGN = 'DES'
    DEVELOPMENT = 'DEV'
    PROJECT_TYPE = [
        (DESIGN, 'Design'),
        (DEVELOPMENT, 'Development'),
    ]

    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    project_type = models.CharField(max_length=3, choices=PROJECT_TYPE, default=DEVELOPMENT, blank=True,  null=True)
    image = models.ImageField(null=True, blank=True, upload_to=project_path)
    about = models.TextField(blank=True, null=True)
    
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    brief = models.TextField(blank=True, null=True)
    
    banner_textI = models.TextField(blank=True, null=True)
    banner_textII = models.TextField(blank=True, null=True)
    banner_textIII = models.TextField(blank=True, null=True)
    
    fullpage_imgI = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgII = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgIII = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgIV = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgV = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgVI = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgVII = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgVIII = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgIX = models.ImageField(null=True, blank=True, upload_to=project_path)
    fullpage_imgX = models.ImageField(null=True, blank=True, upload_to=project_path)
    
    processI = models.TextField(null=True, blank=True)
    processII = models.TextField(null=True, blank=True)
    processIII = models.TextField(null=True, blank=True)
    
    responsive_imgI = models.ImageField(null=True, blank=True, upload_to=project_path)
    responsive_imgII = models.ImageField(null=True, blank=True, upload_to=project_path)
    responsive_imgIII = models.ImageField(null=True, blank=True, upload_to=project_path)
    
    mockup_imgI = models.ImageField(null=True, blank=True, upload_to=project_path)
    mockup_imgII = models.ImageField(null=True, blank=True, upload_to=project_path)
    mockup_imgIII = models.ImageField(null=True, blank=True, upload_to=project_path)
    
    asset_imgI = models.ImageField(null=True, blank=True, upload_to=project_path)
    asset_imgII = models.ImageField(null=True, blank=True, upload_to=project_path)
    asset_imgIII = models.ImageField(null=True, blank=True, upload_to=project_path)
    
    processIV = models.TextField(null=True, blank=True)
    processV = models.TextField(null=True, blank=True)
    processVI = models.TextField(null=True, blank=True)
    processVII = models.TextField(null=True, blank=True)
    processVIII = models.TextField(null=True, blank=True)
    processIX = models.TextField(null=True, blank=True)
    processX = models.TextField(null=True, blank=True)
    
    conclusion = models.TextField(null=True, blank=True)
    software = models.ManyToManyField(Software, blank=True)
    programs = models.ManyToManyField(Program, blank=True)

    class Meta:
        ordering = ['-created_on']
        
    # def save(self, *args, **kwargs):
    #     if self.name and self.image:
    #         filename = f'{ self.name }{ os.path.splitext(self.image.name)[-1]}'
    #         self.image.name = filename
            
    #         super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # Define get_absolute_url for form submit redirect??

class Design(models.Model):

    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    project_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    banner_img = models.ImageField(null=True, blank=True, upload_to="images/des/", db_column="image")
    brief = models.TextField(blank=True, null=True, db_column="description")
    banner_txtI = models.TextField(blank=True, null=True)
    banner_txtII = models.TextField(blank=True, null=True)
    banner_txtIII = models.TextField(blank=True, null=True)
    fullpage_imgI = models.ImageField(null=True, blank=True, upload_to="images/des/")
    fullpage_imgII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    fullpage_imgIII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    processI = models.TextField(null=True, blank=True)
    processII = models.TextField(null=True, blank=True)
    processIII = models.TextField(null=True, blank=True)
    responsive_imgI = models.ImageField(null=True, blank=True, upload_to="images/des/")
    responsive_imgII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    responsive_imgIII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    mockup_imgI = models.ImageField(null=True, blank=True, upload_to="images/des/")
    mockup_imgII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    mockup_imgIII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    asset_imgI = models.ImageField(null=True, blank=True, upload_to="images/des/")
    asset_imgII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    asset_imgIII = models.ImageField(null=True, blank=True, upload_to="images/des/")
    processIV = models.TextField(null=True, blank=True)
    processV = models.TextField(null=True, blank=True)
    processVI = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='design_projects')
    software = models.ManyToManyField(Software)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

class Development(models.Model):

    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/dev/')
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='development_projects')
    programs = models.ManyToManyField(Program)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

