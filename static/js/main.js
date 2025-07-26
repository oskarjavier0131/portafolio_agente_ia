// Esperar a que el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scrolling para links internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animación de progress bars en skills
    const animateProgressBars = () => {
        const progressBars = document.querySelectorAll('.progress-bar');
        
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';
            
            setTimeout(() => {
                bar.style.width = width;
            }, 500);
        });
    };

    // Intersection Observer para animaciones on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                
                // Si es la sección de skills, animar progress bars
                if (entry.target.querySelector('.progress-bar')) {
                    animateProgressBars();
                }
            }
        });
    }, observerOptions);

    // Observar elementos para animaciones
    document.querySelectorAll('.card, .progress, h2').forEach(el => {
        observer.observe(el);
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;

    window.addEventListener('scroll', () => {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Agregar sombra al navbar al hacer scroll
        if (scrollTop > 50) {
            navbar.classList.add('shadow');
        } else {
            navbar.classList.remove('shadow');
        }

        lastScrollTop = scrollTop;
    });

    // Form handling para contacto (preparado para AJAX)
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleContactForm);
    }

    // Loading state para botones
    const addLoadingState = (button) => {
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Enviando...';
        button.disabled = true;
        
        return () => {
            button.innerHTML = originalText;
            button.disabled = false;
        };
    };

    // Función para manejar formulario de contacto
    function handleContactForm(e) {
        e.preventDefault();
        
        const form = e.target;
        const submitBtn = form.querySelector('button[type="submit"]');
        const removeLoading = addLoadingState(submitBtn);
        
        const formData = new FormData(form);
        
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification('¡Mensaje enviado con éxito!', 'success');
                form.reset();
            } else {
                showNotification('Error al enviar mensaje', 'error');
            }
        })
        .catch(error => {
            showNotification('Error de conexión', 'error');
        })
        .finally(() => {
            removeLoading();
        });
    }

    // Utility function para obtener CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Sistema de notificaciones
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type === 'error' ? 'danger' : 'success'} alert-dismissible fade show position-fixed`;
        notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; max-width: 300px;';
        
        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove después de 5 segundos
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    console.log('Portafolio cargado correctamente ✨');
});