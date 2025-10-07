# The Black Robots Foundation - Estructura del Proyecto

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