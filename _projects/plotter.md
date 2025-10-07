---
layout: default
title: "CNC Plotter"
description: "Plotter CNC de bajo costo para dibujo y grabado con firmware personalizado"
slug: "plotter"
status: "Beta"
icon: "fas fa-draw-polygon"
technologies:
  - "Arduino"
  - "G-code"
  - "Vue.js"
  - "WebSocket"
  - "3D Printing"
repository: "https://github.com/TheBlackRobotsFoundation/cnc-plotter"
progress: 85
contributors: 3
stars: 41
---

<div class="container">
  <div class="project-hero">
    <div class="project-header">
      <div class="project-icon large">
        <i class="{{ page.icon }}"></i>
      </div>
      <div class="project-meta">
        <h1>{{ page.title }}</h1>
        <p class="project-description">{{ page.description }}</p>
        <div class="project-badges">
          <span class="badge badge-success">{{ page.status }}</span>
          <span class="badge badge-primary">{{ page.progress }}% Completo</span>
        </div>
      </div>
    </div>
    
    <div class="project-actions">
      <a href="{{ page.repository }}" target="_blank" class="btn btn-primary">
        <i class="fab fa-github"></i>
        Ver en GitHub
      </a>
      <a href="#download" class="btn btn-outline">
        <i class="fas fa-download"></i>
        Descargar Release
      </a>
    </div>
  </div>

  <div class="project-content">
    <section class="content-section">
      <h2>Descripción del Proyecto</h2>
      <p>
        El CNC Plotter es una máquina de dibujo y grabado de bajo costo diseñada para makers, 
        estudiantes y profesionales. Combina precisión mecánica con un firmware personalizado 
        y una interfaz web intuitiva.
      </p>
      
      <h3>Características Principales</h3>
      <ul>
        <li>Área de trabajo configurable hasta 300x300mm</li>
        <li>Precisión de 0.1mm en ambos ejes</li>
        <li>Interfaz web para control remoto</li>
        <li>Soporte para múltiples formatos (SVG, G-code, DXF)</li>
        <li>Diseño modular y actualizable</li>
        <li>Partes impresas en 3D disponibles</li>
      </ul>
    </section>

    <section class="content-section">
      <h2>Tecnologías Utilizadas</h2>
      <div class="tech-grid">
        {% for tech in page.technologies %}
          <div class="tech-item">
            <span class="tag">{{ tech }}</span>
          </div>
        {% endfor %}
      </div>
    </section>

    <section class="content-section" id="download">
      <h2>Descargas y Releases</h2>
      <div class="download-options">
        <div class="card">
          <h4>🔧 Firmware v2.1.0</h4>
          <p>Última versión estable del firmware para Arduino.</p>
          <a href="{{ page.repository }}/releases" target="_blank" class="btn btn-small btn-primary">
            Descargar
          </a>
        </div>
        
        <div class="card">
          <h4>🖥️ Interfaz Web v1.3.2</h4>
          <p>Aplicación web para control del plotter.</p>
          <a href="{{ page.repository }}/releases" target="_blank" class="btn btn-small btn-primary">
            Descargar
          </a>
        </div>
        
        <div class="card">
          <h4>📄 Archivos 3D Print</h4>
          <p>STL y archivos de corte para todas las partes.</p>
          <a href="{{ page.repository }}/tree/main/hardware" target="_blank" class="btn btn-small btn-outline">
            Ver Archivos
          </a>
        </div>
      </div>
    </section>

    <section class="content-section">
      <h2>Estado del Proyecto</h2>
      <div class="project-progress">
        <div class="progress-bar">
          <div class="progress-fill" style="width: {{ page.progress }}%"></div>
        </div>
        <p>{{ page.progress }}% Completo - En fase Beta</p>
      </div>
      
      <div class="project-stats">
        <div class="stat-item">
          <span class="stat-number">{{ page.contributors }}</span>
          <span class="stat-label">Contribuidores</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">{{ page.stars }}</span>
          <span class="stat-label">GitHub Stars</span>
        </div>
      </div>
    </section>
  </div>
</div>