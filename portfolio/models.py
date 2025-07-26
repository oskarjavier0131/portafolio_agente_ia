from django.db import models
from django.utils import timezone

class Skill(models.Model):
    SKILL_TYPES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('ai', 'AI/ML'),
    )
    
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    proficiency = models.IntegerField(default=50)  # 0-100
    icon = models.CharField(max_length=50, blank=True)  # Para íconos CSS
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/', blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    technologies = models.ManyToManyField(Skill)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"

