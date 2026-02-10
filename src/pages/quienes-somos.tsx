import React from 'react';
import Layout from '@theme/Layout';
import styles from './quienes-somos.module.css';

// TODO: Agregar miembros del equipo
const teamMembers = [
  {
    name: 'Nombre Apellido',
    role: 'Fundador / Desarrollador',
    description: 'Breve descripción de experiencia y rol en la fundación.',
    github: 'https://github.com/usuario',
    linkedin: 'https://linkedin.com/in/usuario',
    email: 'email@ejemplo.com',
  },
  // Agregar más miembros aquí
];

function TeamMember({name, role, description, github, linkedin, email}) {
  return (
    <div className={styles.memberCard}>
      <div className={styles.memberAvatar}>
        <div className={styles.avatarPlaceholder}>
          {name.charAt(0)}
        </div>
      </div>
      <h3 className={styles.memberName}>{name}</h3>
      <p className={styles.memberRole}>{role}</p>
      <p className={styles.memberDescription}>{description}</p>
      <div className={styles.memberLinks}>
        {github && (
          <a href={github} target="_blank" rel="noopener noreferrer" className={styles.socialLink}>
            GitHub
          </a>
        )}
        {linkedin && (
          <a href={linkedin} target="_blank" rel="noopener noreferrer" className={styles.socialLink}>
            LinkedIn
          </a>
        )}
        {email && (
          <a href={`mailto:${email}`} className={styles.socialLink}>
            Email
          </a>
        )}
      </div>
    </div>
  );
}

export default function QuienesSomos() {
  return (
    <Layout
      title="Quiénes Somos"
      description="Equipo de The Black Robots Foundation">
      <div className={styles.aboutContainer}>
        <div className="container">
          <div className={styles.aboutHeader}>
            <h1>Quiénes Somos</h1>
            <p>
              Somos un equipo de apasionados por la robótica, compartiendo 
              conocimiento y proyectos open source para hacer la robótica 
              más accesible.
            </p>
          </div>
          
          <div className={styles.teamGrid}>
            {teamMembers.map((member, idx) => (
              <TeamMember key={idx} {...member} />
            ))}
          </div>
          
          <div className={styles.contactSection}>
            <h2>Contacto General</h2>
            <p>
              Para colaboraciones, consultas o más información:
            </p>
            <a href="mailto:contacto@theblackrobots.org" className={styles.contactEmail}>
              contacto@theblackrobots.org
            </a>
          </div>
        </div>
      </div>
    </Layout>
  );
}
