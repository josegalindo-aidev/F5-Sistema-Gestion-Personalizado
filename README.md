
# 🚀 Sistema de Gestión Personalizado

**Solución de software para digitalizar y optimizar la gestión de pequeños y medianos negocios.**
Las indicaciones del ejercicio se encuentran bajo el siguiente enlace
https://github.com/Factoria-F5-madrid/IA-Project-CRUD

![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)
![Metodología](https://img.shields.io/badge/Metodología-TDD%20%7C%20Agile-green)

> **Nota:** El lenguaje, framework, base de datos y demás tecnologías de implementación están pendientes de decisión por parte del equipo. Este documento se actualizará después de la reunión técnica.

---

## 📋 Contenido

1. [Descripción del proyecto](#1-descripción-del-proyecto)
2. [Problema que resuelve](#2-problema-que-resuelve)
3. [Objetivos y funcionalidades](#3-objetivos-y-funcionalidades)
4. [Arquitectura del sistema](#4-arquitectura-del-sistema)
5. [Tecnologías](#5-tecnologías)
6. [Modelo entidad-relación](#6-modelo-entidad-relación)
7. [Instalación y configuración](#7-instalación-y-configuración)
8. [Ejecución del proyecto](#8-ejecución-del-proyecto)
9. [Pruebas y calidad](#9-pruebas-y-calidad)
10. [Documentación](#10-documentación)
11. [Equipo de desarrollo](#11-equipo-de-desarrollo)
12. [Metodología de trabajo](#12-metodología-de-trabajo)
13. [Roadmap y estado del proyecto](#13-roadmap-y-estado-del-proyecto)

---

## 1. Descripción del proyecto

Sistema de Gestión Personalizado es un proyecto de desarrollo de software orientado a facilitar la digitalización y gestión de pequeños y medianos negocios.

El objetivo es construir una aplicación que permita centralizar información, organizar procesos de negocio y mejorar la eficiencia de las operaciones mediante una solución tecnológica adaptada a los requisitos que se definan con el equipo.

El proyecto se desarrollará aplicando buenas prácticas de ingeniería de software, una arquitectura mantenible, pruebas automatizadas y una metodología de trabajo ágil.

## 2. Problema que resuelve

Muchos pequeños y medianos negocios gestionan sus operaciones mediante herramientas dispersas, hojas de cálculo o procedimientos manuales. Esto puede provocar:

- Información duplicada o desactualizada.
- Dificultades para mantener la trazabilidad de los datos.
- Procesos manuales susceptibles de errores.
- Falta de centralización de la información.
- Dificultades para consultar y gestionar los datos del negocio.

El proyecto pretende abordar estas necesidades mediante una solución centralizada. El alcance concreto se establecerá a partir de los requisitos y las historias de usuario acordadas.

## 3. Objetivos y funcionalidades

### Objetivos principales

- Centralizar la información relevante para el negocio.
- Digitalizar los procesos de gestión que se prioricen.
- Facilitar el acceso, consulta y mantenimiento de los datos.
- Construir una solución modular y mantenible.
- Garantizar la calidad mediante pruebas automatizadas.
- Entregar funcionalidades incrementales que respondan a necesidades reales.

### Funcionalidades

Las funcionalidades definitivas se concretarán mediante historias de usuario priorizadas en el Product Backlog.

- Pendiente de definición por el equipo.
- Pendiente de definición por el equipo.
- Pendiente de definición por el equipo.

## 4. Arquitectura del sistema

La arquitectura se definirá en función de los requisitos funcionales y no funcionales, así como de las decisiones tecnológicas que adopte el equipo.

Como orientación inicial, se propone una organización modular por responsabilidades, separando las reglas de negocio de los detalles de presentación, persistencia e infraestructura.

La estructura de referencia prevista es:

```text
src/
└── business_app/
    ├── api/              # Adaptadores de entrada / interfaz
    ├── application/      # Casos de uso y servicios de aplicación
    ├── core/             # Configuración y componentes comunes
    ├── domain/           # Entidades y reglas de negocio
    ├── repositories/     # Contratos de persistencia
    └── infrastructure/  # Implementaciones técnicas
tests/
├── unit/
└── integration/
```

Esta estructura es una propuesta inicial y podrá ajustarse cuando se acuerden la arquitectura y las tecnologías definitivas.

## 5. Tecnologías

**Pendientes de selección y aprobación por el equipo.**

En la próxima reunión técnica se evaluarán y acordarán, entre otros, los siguientes elementos:

| Área | Decisión |
|---|---|
| Lenguaje de programación | Pendiente |
| Framework / tecnología de backend | Pendiente |
| Tipo de interfaz y API | Pendiente |
| Base de datos | Pendiente |
| ORM o mecanismo de acceso a datos | Pendiente |
| Gestión de migraciones | Pendiente |
| Framework de pruebas | Pendiente |
| Análisis estático y formato | Pendiente |
| Integración continua (CI) | Pendiente |

Las decisiones adoptadas se registrarán en la documentación técnica del proyecto para mantener la trazabilidad de los acuerdos.

## 6. Modelo entidad-relación

El modelo entidad-relación describirá las entidades principales del sistema, sus atributos, relaciones y restricciones.

El diseño se realizará una vez concretados los requisitos y el alcance funcional.

**Diagrama del modelo de datos:** pendiente de elaboración.

La documentación correspondiente se incorporará en `docs/database.md`.

## 7. Instalación y configuración

Las instrucciones definitivas de instalación se publicarán después de seleccionar las tecnologías y definir el entorno de desarrollo.

### Requisitos previos

Pendientes de confirmar. Como mínimo, se documentarán:

- Herramientas de control de versiones.
- Lenguaje y versión necesarios.
- Gestor de dependencias.
- Servicios externos o de infraestructura requeridos.

### Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd F5-Sistema-Gestion-Personalizado
```

### Configuración del entorno

Los pasos para crear el entorno, instalar dependencias y configurar las variables locales se añadirán cuando se haya definido el stack tecnológico.

Los secretos, contraseñas y credenciales deberán mantenerse fuera del repositorio. Cuando corresponda, se proporcionará un archivo `.env.example` con las variables necesarias y sin valores sensibles.

## 8. Ejecución del proyecto

El comando de arranque y las instrucciones de ejecución se documentarán cuando esté implementada la aplicación y se haya elegido la tecnología correspondiente.

## 9. Pruebas y calidad

El equipo establecerá una estrategia de pruebas automatizadas coherente con la arquitectura y las tecnologías seleccionadas.

Se aplicará el ciclo TDD:

1. **Red:** escribir una prueba que describa el comportamiento esperado y comprobar que falla.
2. **Green:** implementar el código mínimo necesario para superar la prueba.
3. **Refactor:** mejorar el diseño y la calidad del código manteniendo las pruebas en verde.

Los comandos para ejecutar las pruebas, medir cobertura y realizar análisis de calidad se incorporarán una vez seleccionadas las herramientas.

## 10. Documentación

La documentación técnica y funcional se organizará en el directorio `docs/`.

| Documento | Descripción |
|---|---|
| `docs/architecture.md` | Arquitectura y organización de componentes. |
| `docs/database.md` | Modelo de datos y persistencia. |
| `docs/api.md` | Contratos e interfaces de la API, si aplica. |
| `docs/development-guide.md` | Preparación del entorno y guía de desarrollo. |
| `docs/testing.md` | Estrategia de pruebas y TDD. |
| `docs/workflow.md` | Flujo de trabajo y colaboración. |
| `docs/retrospective.md` | Aprendizajes y mejoras del equipo. |
| `docs/decisions/` | Registro de decisiones técnicas y arquitectónicas (ADR). |

Los documentos se irán completando conforme se tomen decisiones y avance el desarrollo.

## 11. Equipo de desarrollo

| Integrante | GitHub | Responsabilidad |
|---|---|---|
| Yang | [ZhouYangYang1519](https://github.com/ZhouYangYang1519) | Pendiente |
| Marco | [marcosadhwani](https://github.com/marcosadhwani) | Pendiente |
| Integrante 3 | Pendiente | Pendiente |
| Jose | [josegalindo-aidev](https://github.com/josegalindo-aidev) | Pendiente |

Las responsabilidades se definirán de forma colaborativa y podrán evolucionar durante el proyecto.

## 12. Metodología de trabajo

El equipo trabajará siguiendo principios ágiles, con un enfoque iterativo e incremental. La planificación y priorización se gestionarán mediante un backlog y un tablero de trabajo compartido.

### Flujo de trabajo propuesto

1. Seleccionar una historia de usuario priorizada.
2. Crear una rama de trabajo a partir de la rama principal.
3. Escribir primero la prueba correspondiente (Red).
4. Implementar lo mínimo necesario para superarla (Green).
5. Refactorizar y mantener las pruebas en verde.
6. Ejecutar las pruebas y las comprobaciones de calidad.
7. Abrir una Pull Request (PR).
8. Obtener revisión y superar las comprobaciones de integración continua, cuando estén configuradas.
9. Integrar los cambios en la rama principal.

### Convención de ramas

Se propone utilizar los siguientes prefijos:

- `feature/<issue>-<descripcion>`: nuevas funcionalidades.
- `fix/<issue>-<descripcion>`: correcciones.
- `test/<issue>-<descripcion>`: pruebas.
- `docs/<issue>-<descripcion>`: documentación.

Los nombres deberán utilizar minúsculas, números y guiones, evitando espacios y caracteres especiales.

### Convención de commits

Se propone utilizar *Conventional Commits:*

- `feat:` nuevas funcionalidades.
- `fix:` correcciones.
- `test:` incorporación o modificación de pruebas.
- `docs:` documentación.
- `refactor:` mejoras internas sin cambios funcionales.
- `chore:` tareas de mantenimiento y configuración.

### Principios de trabajo

- Priorizar las historias de usuario y los requisitos acordados.
- Mantener el alcance funcional bajo control.
- Evitar complejidad innecesaria y funcionalidades sin valor claro.
- Favorecer la colaboración y la revisión de código.
- Mantener la calidad mediante TDD y automatización.
- Registrar las decisiones técnicas relevantes.

## 13. Roadmap y estado del proyecto

El desarrollo se organizará de forma incremental, priorizando la entrega de funcionalidades que aporten valor al usuario.

| Fase | Objetivo | Estado |
|---|---|---|
| 1. Preparación | Repositorio, estructura inicial y organización del equipo. | En curso |
| 2. Definición | Requisitos, alcance y selección tecnológica. | Pendiente |
| 3. Diseño | Arquitectura y modelo de datos. | Pendiente |
| 4. Desarrollo | Implementación de funcionalidades priorizadas mediante TDD. | Pendiente |
| 5. Integración y validación | Integración de módulos y pruebas de conjunto. | Pendiente |
| 6. Entrega | Documentación, validación y demostración del producto. | Pendiente |

El estado de las fases y funcionalidades se actualizará conforme avance el trabajo.

---

**Proyecto desarrollado en el contexto del Bootcamp Factoria F5.**
