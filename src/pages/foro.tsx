import React from 'react';
import Layout from '@theme/Layout';
import Giscus from '@giscus/react';
import styles from './foro.module.css';

export default function Foro() {
  return (
    <Layout
      title="Foro"
      description="Foro de la comunidad Black Robots Foundation">
      <div className={styles.foroContainer}>
        <div className="container">
          <div className={styles.foroHeader}>
            <h1>Foro de la Comunidad</h1>
            <p>
              Pregunta, comparte tus proyectos, reporta problemas o simplemente 
              charla sobre robótica con la comunidad.
            </p>
          </div>
          
          <div className={styles.giscusWrapper}>
            <Giscus
              repo="TheBlackRobotsFoundation/theblackrobotsfoundation.github.io"
              repoId="R_kgDOP9fGWg"
              category="General"
              categoryId="DIC_kwDOP9fGWs4C2HDt"
              mapping="specific"
              term="foro-comunidad"
              strict="0"
              reactionsEnabled="1"
              emitMetadata="0"
              inputPosition="bottom"
              theme="dark_high_contrast"
              lang="es"
              loading="lazy"
            />
          </div>
        </div>
      </div>
    </Layout>
  );
}
