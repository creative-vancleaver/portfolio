from django.db import models

from jvc_portfolio.models import Program

# Create your models here.

class About(models.Model):
    
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.pk

class SupplimentalEducation(models.Model):

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

class TechnicalSkills(models.Model):

    type = models.CharField(max_length=200)
    programs = models.ManyToManyField(Program)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.type

class PorgrammingProjects(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

class Employment(models.Model):

    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    job_title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

