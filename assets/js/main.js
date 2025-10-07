/**
 * BlackRobots Foundation - Main JavaScript
 * Handles navigation, mobile menu, and interactive elements
 */

(function() {
  'use strict';

  // DOM Elements
  const mobileToggle = document.getElementById('mobile-toggle');
  const sidebar = document.getElementById('sidebar');
  const sidebarToggle = document.getElementById('sidebar-toggle');
  const sidebarOverlay = document.getElementById('sidebar-overlay');

  // Mobile Navigation Toggle
  if (mobileToggle) {
    mobileToggle.addEventListener('click', function() {
      sidebar?.classList.toggle('open');
      sidebarOverlay?.classList.toggle('show');
      document.body.style.overflow = sidebar?.classList.contains('open') ? 'hidden' : '';
    });
  }

  // Sidebar Toggle (Close)
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', function() {
      sidebar?.classList.remove('open');
      sidebarOverlay?.classList.remove('show');
      document.body.style.overflow = '';
    });
  }

  // Sidebar Overlay Click (Close)
  if (sidebarOverlay) {
    sidebarOverlay.addEventListener('click', function() {
      sidebar?.classList.remove('open');
      sidebarOverlay?.classList.remove('show');
      document.body.style.overflow = '';
    });
  }

  // Close sidebar on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && sidebar?.classList.contains('open')) {
      sidebar.classList.remove('open');
      sidebarOverlay?.classList.remove('show');
      document.body.style.overflow = '';
    }
  });

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
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

  // Project card hover effects
  const projectCards = document.querySelectorAll('.project-card');
  projectCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-4px)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });

  // Add loading states for external links
  document.querySelectorAll('a[target="_blank"]').forEach(link => {
    link.addEventListener('click', function() {
      // Add loading indicator or animation if needed
      console.log('Opening external link:', this.href);
    });
  });

  // Lazy loading for images (if any)
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

  // Tech items animation enhancement
  const techItems = document.querySelectorAll('.tech-item');
  if (techItems.length > 0 && 'IntersectionObserver' in window) {
    const techObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.style.animationPlayState = 'running';
          }, index * 100);
        }
      });
    }, { threshold: 0.5 });

    techItems.forEach(item => {
      item.style.animationPlayState = 'paused';
      techObserver.observe(item);
    });
  }

  // Console welcome message
  console.log(`
    🤖 BlackRobots Foundation
    ========================
    Welcome to our open source robotics community!
    
    Interested in contributing? 
    Visit: https://github.com/TheBlackRobotsFoundation
    
    Found a bug? Please report it!
    Email: contact@blackrobots.org
  `);

  // Theme detection (for future dark/light mode toggle)
  const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
  
  // Handle theme changes
  prefersDarkScheme.addEventListener('change', (e) => {
    // Currently always dark theme, but ready for future enhancement
    console.log('Color scheme preference changed:', e.matches ? 'dark' : 'light');
  });

  // Performance monitoring (basic)
  window.addEventListener('load', () => {
    const loadTime = performance.now();
    console.log(`Page loaded in ${Math.round(loadTime)}ms`);
    
    // Send to analytics if needed
    if (typeof gtag !== 'undefined') {
      gtag('event', 'page_load_time', {
        value: Math.round(loadTime)
      });
    }
  });

  // Error handling for failed resource loads
  window.addEventListener('error', (e) => {
    console.error('Resource failed to load:', e.target);
    
    // Handle missing images gracefully
    if (e.target.tagName === 'IMG') {
      e.target.style.display = 'none';
    }
  });

})();