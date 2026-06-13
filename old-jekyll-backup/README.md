# BlackRobots Foundation Website

🤖 Sitio web oficial de la BlackRobots Foundation - Una comunidad open source dedicada al desarrollo de tecnología robótica accesible.

## 🚀 Desarrollo con Jekyll

Este sitio está construido con [Jekyll](https://jekyllrb.com/), un generador de sitios estáticos que permite crear sitios web profesionales y fáciles de mantener.

### Prerrequisitos

- Ruby (versión 2.7 o superior)
- Bundler gem
- Git

### Instalación Local

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/TheBlackRobotsFoundation/theblackrobotsfoundation.github.io.git
   cd theblackrobotsfoundation.github.io
   ```

2. **Instala las dependencias:**
   ```bash
   bundle install
   ```

3. **Ejecuta el servidor de desarrollo:**
   ```bash
   bundle exec jekyll serve
   ```

4. **Abre tu navegador en:**
   ```
   http://localhost:4000
   ```

### Comandos Útiles

- **Desarrollo con recarga automática:**
  ```bash
  bundle exec jekyll serve --livereload
  ```

- **Construir para producción:**
  ```bash
  bundle exec jekyll build
  ```

- **Limpiar archivos generados:**
  ```bash
  bundle exec jekyll clean
  ```

## 📁 Estructura del Proyecto

```
├── _config.yml          # Configuración principal de Jekyll
├── _layouts/            # Plantillas HTML base
├── _includes/           # Componentes reutilizables
├── _sass/              # Archivos SCSS modulares
├── _data/              # Datos del sitio (YAML)
├── _projects/          # Colección de proyectos
├── assets/             # CSS, JS e imágenes
├── index.html          # Página principal
├── Gemfile            # Dependencias Ruby
└── README.md          # Este archivo
```

## 🎨 Personalización

### Colores y Tema

Los colores se definen en `_sass/_variables.scss`:

```scss
$bg-primary: #0A0A0A;     // Fondo principal (negro)
$bg-secondary: #111111;    // Fondo secundario
$accent: #00E5FF;         // Color de acento (cyan)
```

### Contenido

1. **Proyectos:** Edita `_data/projects.yml` para añadir/modificar proyectos
2. **Navegación:** Modifica `_config.yml` en la sección `navigation`
3. **Páginas:** Crea archivos `.md` o `.html` en el directorio raíz

## 🚀 Despliegue

Este sitio se despliega automáticamente en GitHub Pages cuando se hace push a la rama `main`.

## 🤝 Contribuir

1. Fork este repositorio
2. Crea una rama para tu feature
3. Haz commit de tus cambios
4. Crea un Pull Request

## 📝 Licencia

MIT License - ver el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">
  Hecho con ❤️ por la <strong>BlackRobots Foundation</strong>
</div>

## 📁 Estructura de Carpetas

```
theblackrobotsfoundation.github.io/
├── 📄 index.html                    # Página principal
├── 📄 CNAME                        # Configuración GitHub Pages
├── 📄 LICENSE                      # Licencia del proyecto
├── 📄 README.md                    # Documentación del proyecto
│
├── 📁 assets/                      # Recursos estáticos
│   ├── 📁 css/                     # Hojas de estilo
│   │   ├── 📄 main.css             # Estilos principales
│   │   ├── 📄 variables.css        # Variables CSS y tema
│   │   ├── 📄 components.css       # Estilos de componentes
│   │   └── 📄 responsive.css       # Media queries
│   │
│   ├── 📁 js/                      # Scripts JavaScript
│   │   ├── 📄 main.js              # JavaScript principal
│   │   ├── 📄 navigation.js        # Lógica de navegación
│   │   └── 📄 utils.js             # Utilidades
│   │
│   ├── 📁 fonts/                   # Fuentes personalizadas
│   │   ├── 📄 fonts.css            # Declaraciones @font-face
│   │   └── 📁 files/               # Archivos de fuentes (.woff2, .woff, etc.)
│   │
│   └── 📁 images/                  # Imágenes y gráficos
│       ├── 📁 icons/               # Iconos SVG
│       ├── 📁 projects/            # Imágenes de proyectos
│       └── 📁 logos/               # Logos y branding
│
├── 📁 pages/                       # Páginas individuales
│   ├── 📄 about.html               # Quiénes somos
│   ├── 📄 contribute.html          # Cómo contribuir
│   ├── 📄 forum.html               # Foro/comunidad
│   └── 📄 404.html                 # Página de error
│
├── 📁 projects/                    # Documentación de proyectos
│   ├── 📁 the-drone/               # Proyecto The Drone
│   │   ├── 📄 index.html           # Página principal del proyecto
│   │   ├── 📄 documentation.html   # Documentación técnica
│   │   ├── 📄 gallery.html         # Galería de imágenes
│   │   └── 📁 files/               # Archivos del proyecto
│   │
│   └── 📁 the-plotter/             # Proyecto The Plotter
│       ├── 📄 index.html           # Página principal del proyecto
│       ├── 📄 documentation.html   # Documentación técnica
│       ├── 📄 gallery.html         # Galería de imágenes
│       └── 📁 files/               # Archivos del proyecto
│
└── 📁 components/                  # Componentes reutilizables
    ├── 📄 header.html              # Header con navegación
    ├── 📄 sidebar.html             # Sidebar de proyectos
    ├── 📄 footer.html              # Footer
    └── 📄 project-card.html        # Card de proyecto
```

## 🎨 Sistema de Fuentes Personalizadas

### Ubicación
- Archivos de fuentes: `assets/fonts/files/`
- Configuración: `assets/fonts/fonts.css`

### Formatos Recomendados
1. **WOFF2** - Mejor compresión, soporte moderno
2. **WOFF** - Fallback para navegadores más antiguos
3. **TTF** - Fallback adicional

### Ejemplo de Uso
```css
/* En fonts.css */
@font-face {
  font-family: 'MiFuenteCustom';
  src: url('./files/MiFuente-Regular.woff2') format('woff2'),
       url('./files/MiFuente-Regular.woff') format('woff');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

## 🔧 Configuración de Desarrollo

### Estructura CSS Modular
- **variables.css**: Colores, espaciado, tipografía
- **main.css**: Estilos base y layout principal
- **components.css**: Estilos de componentes individuales
- **responsive.css**: Media queries y responsive design

### JavaScript Modular
- **main.js**: Inicialización y funciones principales
- **navigation.js**: Lógica de menús y navegación
- **utils.js**: Funciones utilitarias reutilizables

## 📱 Responsive Design

Breakpoints recomendados:
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px  
- **Desktop**: > 1024px
- **Large Desktop**: > 1440px

## 🚀 Deployment

Este proyecto está configurado para GitHub Pages. Los archivos se sirven directamente desde la rama principal.

## 📝 Convenciones de Código

- **HTML**: Semántico y accesible
- **CSS**: Metodología BEM para clases
- **JavaScript**: ES6+ con módulos
- **Archivos**: Nombres en kebab-case

## 🤝 Contribución

Ver `pages/contribute.html` para guías de contribución detalladas.