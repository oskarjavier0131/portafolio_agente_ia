from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Experience

def home(request):
    """Página principal con proyectos destacados"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """Página sobre mí"""
    experiences = Experience.objects.all()
    skills_by_type = {}
    
    for skill in Skill.objects.all():
        if skill.skill_type not in skills_by_type:
            skills_by_type[skill.skill_type] = []
        skills_by_type[skill.skill_type].append(skill)
    
    context = {
        'experiences': experiences,
        'skills_by_type': skills_by_type,
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    """Todos los proyectos"""
    all_projects = Project.objects.all()
    context = {'projects': all_projects}
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, pk):
    """Detalle de un proyecto específico"""
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}
    return render(request, 'portfolio/project_detail.html', context)

def contact(request):
    """Página de contacto"""
    if request.method == 'POST':
        # Procesar formulario de contacto
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Aquí después agregaremos envío de email
        # Por ahora solo retornamos success
        return JsonResponse({'success': True})
    
    return render(request, 'portfolio/contact.html')

# Create your views here.
