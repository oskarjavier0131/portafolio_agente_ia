from django.contrib import admin
from .models import Skill, Project, Experience

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill_type', 'proficiency']
    list_filter = ['skill_type']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_date']
    list_filter = ['featured', 'technologies']
    filter_horizontal = ['technologies']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'current']
    list_filter = ['current']
# Register your models here.
