import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  description: ReactNode;
  image: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Open Source',
    image: '/img/feature-opensource.png',
    description: (
      <>
        Todos nuestros proyectos son completamente open source. 
        Código, esquemas y diseños disponibles para toda la comunidad.
      </>
    ),
  },
  {
    title: 'Diseño Minimalista',
    image: '/img/feature-design.png',
    description: (
      <>
        Estética cuidada y funcional. Simplicidad sin comprometer 
        rendimiento ni calidad en cada proyecto.
      </>
    ),
  },
  {
    title: 'Reinventando la Robótica',
    image: '/img/feature-robotics.png',
    description: (
      <>
        Nuevas formas de hacer robótica accesible. Documentación clara, 
        proyectos modulares y aprendizaje práctico.
      </>
    ),
  },
];

function Feature({title, image, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className={styles.featureCard}>
        <div className="text--center">
          <img src={image} alt={title} className={styles.featureImage} />
        </div>
        <div className="text--center padding-horiz--md">
          <Heading as="h3">{title}</Heading>
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
