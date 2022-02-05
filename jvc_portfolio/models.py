from django.db import models

# Create your models here.

class Project(models.Model):

    DESIGN = 'DES'
    DEVELOPMENT = 'DEV'
    PROJECT_TYPE = [
        (DESIGN, 'Design'),
        (DEVELOPMENT, 'Development'),
    ]

    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    project_type = models.CharField(max_length=3, choices=PROJECT_TYPE, default=DEVELOPMENT)
    about = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # Define get_absolute_url for form submit redirect??


class Software(models.Model):

    # CAN EASILY ADD TO CHOICES AS I LEARN/USE THEM
    # PHOTOSHOP = 'PS'
    # ILLUSTRATOR = 'AI'
    # LR = 'Lightroom'
    # SOFTWARE = [
    #     (PHOTOSHOP, 'Photoshop'),
    #     (ILLUSTRATOR, 'Illustrator'),
    #     (LR, 'Lightroom'),
    # ]

    name = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Software'

    def __str__(self):
        return self.name
    
class Design(models.Model):

    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/des/")
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='design_projects')
    software = models.ManyToManyField(Software)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

class Program(models.Model):

    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name



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

