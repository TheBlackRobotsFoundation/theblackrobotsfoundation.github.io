/* =========================================
   THE BLACK ROBOTS FOUNDATION - MAIN SCRIPT
   JavaScript para navegación y interacciones
========================================= */

document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    initializeSidebar();
    initializeScrollEffects();
    initializeProjectCards();
});

/* =========================================
   NAVEGACIÓN PRINCIPAL
========================================= */
function initializeNavigation() {
    const mobileToggle = document.getElementById('mobile-toggle');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    
    // Toggle móvil para sidebar
    if (mobileToggle) {
        mobileToggle.addEventListener('click', function() {
            toggleSidebar();
        });
    }
    
    // Overlay para cerrar sidebar en móvil
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', function() {
            closeSidebar();
        });
    }
    
    // Cerrar sidebar con ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeSidebar();
        }
    });
    
    // Navegación suave para enlaces internos
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
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    
    if (sidebar && overlay) {
        sidebar.classList.toggle('open');
        overlay.classList.toggle('show');
        
        // Prevenir scroll del body cuando sidebar está abierto
        if (sidebar.classList.contains('open')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    }
}

function closeSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    
    if (sidebar && overlay) {
        sidebar.classList.remove('open');
        overlay.classList.remove('show');
        document.body.style.overflow = '';
    }
}

/* =========================================
   SIDEBAR DE PROYECTOS
========================================= */
function initializeSidebar() {
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const projectLinks = document.querySelectorAll('.project-link');
    
    // Toggle de cerrar sidebar
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            closeSidebar();
        });
    }
    
    // Activar enlaces de proyectos
    projectLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Remover active de todos los enlaces
            projectLinks.forEach(l => l.classList.remove('active'));
            
            // Activar el enlace clickeado
            this.classList.add('active');
            
            // En móvil, cerrar sidebar después de seleccionar
            if (window.innerWidth <= 768) {
                setTimeout(() => {
                    closeSidebar();
                }, 150);
            }
        });
    });
}

/* =========================================
   EFECTOS DE SCROLL
========================================= */
function initializeScrollEffects() {
    // Efecto de header al hacer scroll
    let lastScrollTop = 0;
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Cambiar opacidad del header
        if (scrollTop > 50) {
            header.style.background = 'rgba(255, 255, 255, 0.98)';
            header.style.boxShadow = '0 1px 3px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.boxShadow = 'none';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Animaciones de aparición con Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observar elementos para animación
    const animateElements = document.querySelectorAll('.project-card, .hero-content, .contribute-content');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });
}

/* =========================================
   TARJETAS DE PROYECTOS
========================================= */
function initializeProjectCards() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        // Efecto hover mejorado
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        // Click en tarjeta para navegar
        card.addEventListener('click', function() {
            const projectLink = this.querySelector('.project-link-btn');
            if (projectLink) {
                projectLink.click();
            }
        });
    });
}

/* =========================================
   ANIMACIÓN DE ESTADÍSTICAS
========================================= */
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const target = parseInt(counter.textContent.replace(/\D/g, ''));
        let current = 0;
        const increment = target / 60; // 60 frames para 1 segundo
        
        const updateCounter = () => {
            if (current < target) {
                current += increment;
                counter.textContent = Math.floor(current) + '+';
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target + '+';
            }
        };
        
        updateCounter();
    });
}

// Activar animación de contadores cuando están visibles
const statsObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
            entry.target.classList.add('animated');
            animateCounters();
        }
    });
}, { threshold: 0.5 });

// Observar sección de estadísticas
document.addEventListener('DOMContentLoaded', function() {
    const statsSection = document.querySelector('.contribute-stats');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
});

/* =========================================
   RESPONSIVE UTILITIES
========================================= */
function handleResize() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    
    // Cerrar sidebar en desktop
    if (window.innerWidth > 768) {
        if (sidebar) sidebar.classList.remove('open');
        if (overlay) overlay.classList.remove('show');
        document.body.style.overflow = '';
    }
}

window.addEventListener('resize', handleResize);

/* =========================================
   TEMA DARK/LIGHT (Opcional)
========================================= */
function initializeThemeToggle() {
    // Detectar preferencia del sistema
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Escuchar cambios en la preferencia del sistema
    prefersDark.addEventListener('change', (e) => {
        if (e.matches) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    });
    
    // Aplicar tema inicial
    if (prefersDark.matches) {
        document.documentElement.classList.add('dark');
    }
}

/* =========================================
   LAZY LOADING DE IMÁGENES
========================================= */
function initializeLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
}

/* =========================================
   PRELOADER (Opcional)
========================================= */
function initializePreloader() {
    window.addEventListener('load', function() {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.style.opacity = '0';
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 300);
        }
        
        // Activar animaciones después de cargar
        document.body.classList.add('loaded');
    });
}

/* =========================================
   COPY TO CLIPBOARD
========================================= */
function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showNotification('Copiado al portapapeles', 'success');
        });
    } else {
        // Fallback para navegadores más antiguos
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showNotification('Copiado al portapapeles', 'success');
    }
}

/* =========================================
   NOTIFICACIONES
========================================= */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Estilos inline para la notificación
    Object.assign(notification.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '12px 24px',
        borderRadius: '6px',
        color: 'white',
        fontWeight: '500',
        zIndex: '9999',
        transform: 'translateX(400px)',
        transition: 'transform 0.3s ease-out',
        backgroundColor: type === 'success' ? '#10B981' : type === 'error' ? '#EF4444' : '#3B82F6'
    });
    
    document.body.appendChild(notification);
    
    // Animar entrada
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remover después de 3 segundos
    setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

/* =========================================
   SCROLL TO TOP
========================================= */
function initializeScrollToTop() {
    const scrollBtn = document.createElement('button');
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollBtn.className = 'scroll-to-top';
    
    // Estilos para el botón
    Object.assign(scrollBtn.style, {
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        width: '50px',
        height: '50px',
        borderRadius: '50%',
        border: 'none',
        backgroundColor: 'var(--color-primary)',
        color: 'white',
        fontSize: '18px',
        cursor: 'pointer',
        opacity: '0',
        visibility: 'hidden',
        transform: 'scale(0)',
        transition: 'all 0.3s ease-out',
        zIndex: '1000',
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
    });
    
    document.body.appendChild(scrollBtn);
    
    // Mostrar/ocultar según scroll
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollBtn.style.opacity = '1';
            scrollBtn.style.visibility = 'visible';
            scrollBtn.style.transform = 'scale(1)';
        } else {
            scrollBtn.style.opacity = '0';
            scrollBtn.style.visibility = 'hidden';
            scrollBtn.style.transform = 'scale(0)';
        }
    });
    
    // Funcionalidad del botón
    scrollBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/* =========================================
   INICIALIZACIÓN ADICIONAL
========================================= */
document.addEventListener('DOMContentLoaded', function() {
    initializeThemeToggle();
    initializeLazyLoading();
    initializePreloader();
    initializeScrollToTop();
});

/* =========================================
   EASTER EGG - KONAMI CODE
========================================= */
let konamiCode = [];
const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65]; // ↑↑↓↓←→←→BA

document.addEventListener('keydown', function(e) {
    konamiCode.push(e.keyCode);
    
    if (konamiCode.length > konamiSequence.length) {
        konamiCode.shift();
    }
    
    if (konamiCode.join(',') === konamiSequence.join(',')) {
        // Easter egg activado!
        document.body.style.animation = 'rainbow 2s infinite';
        showNotification('🤖 ¡Easter egg activado! ¡Bienvenido maker!', 'success');
        
        setTimeout(() => {
            document.body.style.animation = '';
        }, 5000);
        
        console.log('🤖 ¡Konami Code activado! Eres un verdadero maker de Black Robots Foundation!');
    }
});

// CSS para el easter egg
const easterEggStyle = document.createElement('style');
easterEggStyle.textContent = `
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        25% { filter: hue-rotate(90deg); }
        50% { filter: hue-rotate(180deg); }
        75% { filter: hue-rotate(270deg); }
        100% { filter: hue-rotate(360deg); }
    }
`;
document.head.appendChild(easterEggStyle);