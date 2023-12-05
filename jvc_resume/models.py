from django.db import models

from jvc_portfolio.models import Program

# Create your models here.

def bio_path(instance, filename):
    return '/'.join(['images/bio', filename])
class About(models.Model):
    
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to=bio_path)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.pk)

class SupplimentalEducation(models.Model):

    name = models.CharField(max_length=200, blank=True,  null=True)
    type = models.CharField(max_length=200, blank=True,  null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

class TechnicalSkills(models.Model):

    type = models.CharField(max_length=200, blank=True, null=True)
    programs = models.ManyToManyField(Program)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.type

class ProgrammingProjects(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

class Employment(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    start_year = models.CharField(max_length=4, blank=True, null=True)
    end_year = models.CharField(max_length=4, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

