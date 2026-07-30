---
sidebar_position: 5
title: Xacro
sidebar_custom_props:
  icon: /img/guias/iconos/ejemplos.svg
---

# Xacro

Cuando un robot crece, el URDF se llena de piezas casi iguales (cuatro ruedas, dos brazos…) y copiar y pegar XML se vuelve un problema. **Xacro** (*XML Macros*) resuelve esto: escribes plantillas y variables, y genera el URDF final por ti.

Un archivo xacro es un URDF normal que añade tres superpoderes: **variables**, **matemáticas** y **macros**.

## 1. Variables (propiedades)

Defines un valor una vez y lo reutilizas. Si cambia, lo cambias en un solo sitio.

```xml
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="mi_robot">

  <xacro:property name="radio_rueda" value="0.05"/>
  <xacro:property name="ancho_rueda" value="0.02"/>

  <link name="rueda">
    <visual>
      <geometry>
        <cylinder radius="${radio_rueda}" length="${ancho_rueda}"/>
      </geometry>
    </visual>
  </link>

</robot>
```

Todo lo que va entre `${...}` se sustituye por su valor. También admite cuentas: `${radio_rueda * 2}`.

## 2. Incluir otros archivos

Puedes partir el robot en varios archivos y unirlos:

```xml
<xacro:include filename="ruedas.xacro"/>
<xacro:include filename="sensores.xacro"/>
```

Así mantienes cada parte del robot en su propio archivo, ordenado.

## 3. Macros (plantillas reutilizables)

Una **macro** es una plantilla con huecos. Defines una rueda una vez y la "llamas" tantas veces como necesites, cambiando solo lo que varía:

```xml
<!-- Definimos la plantilla de una rueda -->
<xacro:macro name="rueda" params="nombre x y">
  <link name="${nombre}">
    <visual>
      <geometry>
        <cylinder radius="${radio_rueda}" length="${ancho_rueda}"/>
      </geometry>
    </visual>
  </link>
  <joint name="${nombre}_joint" type="continuous">
    <parent link="base_link"/>
    <child link="${nombre}"/>
    <origin xyz="${x} ${y} 0"/>
    <axis xyz="0 1 0"/>
  </joint>
</xacro:macro>

<!-- Y creamos las cuatro ruedas en una línea cada una -->
<xacro:rueda nombre="rueda_del_izq" x="0.2"  y="0.15"/>
<xacro:rueda nombre="rueda_del_der" x="0.2"  y="-0.15"/>
<xacro:rueda nombre="rueda_tra_izq" x="-0.2" y="0.15"/>
<xacro:rueda nombre="rueda_tra_der" x="-0.2" y="-0.15"/>
```

Cuatro ruedas completas, con su joint incluido, en cuatro líneas.

## Convertir xacro a URDF

Las herramientas de ROS leen xacro directamente, pero puedes generar el URDF plano cuando quieras:

```bash
xacro mi_robot.xacro > mi_robot.urdf
```

:::tip
Regla práctica: escribe **xacro** desde el primer día. Un robot pequeño casi no lo nota, pero en cuanto tenga piezas repetidas te ahorra cientos de líneas y errores de copiar y pegar.
:::
