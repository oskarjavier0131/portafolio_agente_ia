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
    
    # Obtener otros proyectos para mostrar como relacionados
    related_projects = Project.objects.exclude(pk=pk)[:3]
    
    context = {
        'project': project,
        'projects': related_projects,  # Para proyectos relacionados
    }
    return render(request, 'portfolio/project_detail.html', context)
    
def contact(request):
    """Página de contacto"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company = request.POST.get('company', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validación básica
        if not all([name, email, subject, message]):
            return JsonResponse({'success': False, 'error': 'Campos requeridos faltantes'})
        
        # Aquí puedes agregar envío de email, guardar en DB, etc.
        # Por ahora solo simulamos éxito
        
        # TODO: Implementar envío de email
        # send_mail(
        #     subject=f'Contacto: {subject}',
        #     message=f'De: {name} ({email})\n\n{message}',
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=['tu@email.com'],
        # )
        
        return JsonResponse({'success': True})
    
    return render(request, 'portfolio/contact.html')
    
