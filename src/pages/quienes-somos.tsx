import React from 'react';
import Layout from '@theme/Layout';
import styles from './quienes-somos.module.css';

const diego = {
  name: 'Diego Rayado',
  role: 'Fundador',
  avatar: '/img/diego.svg',
  description:
    'Aventurero y curioso por naturaleza. La robótica y la electrónica son mi obsesión desde hace años, y Black Robots es mi forma de documentarlo todo, enseñar lo que sé y crear la comunidad que a mí me hubiera gustado encontrar.',
  links: [
    {label: 'GitHub', href: 'https://github.com/TheBlackRobotsFoundation'},
    {label: 'Instagram', href: 'https://instagram.com/diegoo.rrz'},
    {label: 'Email', href: 'mailto:hello@blackrobots.org'},
  ],
};

const brandSocials = [
  {label: 'Instagram', href: 'https://instagram.com/black.robots'},
  {label: 'YouTube', href: 'https://youtube.com/@black.robots'},
  {label: 'TikTok', href: 'https://tiktok.com/@blackrobots'},
];

export default function QuienesSomos() {
  return (
    <Layout
      title="Quiénes Somos"
      description="Sobre Black Robots Foundation">
      <div className={styles.aboutContainer}>
        <div className="container">
          <div className={styles.aboutHeader}>
            <h1>Quiénes Somos</h1>
            <p>
              Black Robots es tu rincón de robótica: proyectos, guías,
              curiosidades y noticias. Todo lo que mola de este mundo, en
              un solo sitio.
            </p>
          </div>

          <div className={styles.teamGrid}>
            <div className={styles.memberCard} style={{maxWidth: 500, margin: '0 auto'}}>
              <div className={styles.memberAvatar}>
                {diego.avatar ? (
                  <img src={diego.avatar} alt={diego.name} className={styles.avatarImg} />
                ) : (
                  <div className={styles.avatarPlaceholder}>{diego.name.charAt(0)}</div>
                )}
              </div>
              <h3 className={styles.memberName}>{diego.name}</h3>
              <p className={styles.memberRole}>{diego.role}</p>
              <p className={styles.memberDescription}>{diego.description}</p>
              <div className={styles.memberLinks}>
                {diego.links.map((l) => (
                  <a
                    key={l.label}
                    href={l.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={styles.socialLink}>
                    {l.label}
                  </a>
                ))}
              </div>
            </div>
          </div>

          <div className={styles.contactSection}>
            <h2>Contacto</h2>
            <p>¿Colaboraciones, dudas o ideas? Escríbeme:</p>
            <a href="mailto:hello@blackrobots.org" className={styles.contactEmail}>
              hello@blackrobots.org
            </a>
            <div className={styles.memberLinks} style={{marginTop: '1.5rem'}}>
              {brandSocials.map((s) => (
                <a
                  key={s.label}
                  href={s.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={styles.socialLink}>
                  {s.label}
                </a>
              ))}
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}
