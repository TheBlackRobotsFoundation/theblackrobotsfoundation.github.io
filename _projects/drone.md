---
layout: default
title: "Drone Project"
description: "Drone autónomo open source con navegación avanzada y visión artificial"
slug: "drone"
status: "En desarrollo"
icon: "fas fa-drone"
technologies:
  - "ROS 2"
  - "Python"
  - "OpenCV"
  - "ArduPilot"
  - "Gazebo"
repository: "https://github.com/TheBlackRobotsFoundation/drone-project"
progress: 60
contributors: 5
stars: 23
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
          <span class="badge badge-warning">{{ page.status }}</span>
          <span class="badge badge-primary">{{ page.progress }}% Completo</span>
        </div>
      </div>
    </div>
    
    <div class="project-actions">
      <a href="{{ page.repository }}" target="_blank" class="btn btn-primary">
        <i class="fab fa-github"></i>
        Ver en GitHub
      </a>
      <a href="#contribute" class="btn btn-outline">
        <i class="fas fa-code-branch"></i>
        Contribuir
      </a>
    </div>
  </div>

  <div class="project-content">
    <section class="content-section">
      <h2>Descripción del Proyecto</h2>
      <p>
        El proyecto de drone tiene como objetivo desarrollar una plataforma de drone autónomo 
        completamente open source. El sistema incluye navegación autónoma, capacidades de mapeo 
        y una interfaz de misiones programables.
      </p>
      
      <h3>Características Principales</h3>
      <ul>
        <li>Navegación autónoma con GPS y sensores</li>
        <li>Sistema de visión artificial para detección de obstáculos</li>
        <li>Planificación de misiones programables</li>
        <li>Interfaz de control remoto</li>
        <li>Telemetría en tiempo real</li>
        <li>Hardware modular y actualizable</li>
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

    <section class="content-section" id="contribute">
      <h2>Cómo Contribuir</h2>
      <p>
        Este proyecto está abierto a contribuciones de la comunidad. Puedes ayudar de las siguientes maneras:
      </p>
      
      <div class="contribute-options">
        <div class="card">
          <h4>💻 Desarrollo de Software</h4>
          <p>Contribuye con código Python, ROS 2, o mejoras en los algoritmos de navegación.</p>
        </div>
        
        <div class="card">
          <h4>🔧 Hardware</h4>
          <p>Ayuda con el diseño de PCB, selección de componentes o mejoras mecánicas.</p>
        </div>
        
        <div class="card">
          <h4>📚 Documentación</h4>
          <p>Mejora la documentación, crea tutoriales o traduce contenido.</p>
        </div>
        
        <div class="card">
          <h4>🧪 Testing</h4>
          <p>Prueba el software, reporta bugs o sugiere mejoras.</p>
        </div>
      </div>
    </section>

    <section class="content-section">
      <h2>Estado del Proyecto</h2>
      <div class="project-progress">
        <div class="progress-bar">
          <div class="progress-fill" style="width: {{ page.progress }}%"></div>
        </div>
        <p>{{ page.progress }}% Completo</p>
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