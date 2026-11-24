
# Architecture Decision Records

Registrar decisiones técnicas relevantes con contexto, opciones, decisión, consecuencias, estado y fecha. No borrar decisiones anteriores; crear un nuevo ADR si cambia una decisión.

---

# ADR-0001: Selección del stack tecnológico

- Estado: Propuesto / pendiente de aprobación
- Fecha: completar
- Decisores: equipo

## Contexto
API REST, persistencia SQL y documentación. Plazo de dos semanas, equipo de 3–4 desarrolladores.

## Opciones
1. FastAPI + PostgreSQL + SQLAlchemy + Alembic.
2. Flask + MySQL + SQLAlchemy + Alembic.
3. Django REST Framework + PostgreSQL.

## Propuesta inicial
FastAPI + PostgreSQL + SQLAlchemy + Alembic por validación, OpenAPI y separación de componentes.

## Consecuencias
La elección afecta dependencias, configuración, persistencia, pruebas y despliegue. No integrar framework ni ORM hasta aprobarlo.

## Decisión final
Pendiente. Registrar opción, justificación y fecha.
