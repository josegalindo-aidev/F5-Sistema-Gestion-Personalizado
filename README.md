# 🚀 Sistema de Gestión Personalizado
API REST · Python · FastAPI · PostgreSQL

Una solución tecnológica diseñada para digitalizar y optimizar la gestión de pequeños y medianos negocios.

## Contenido:
1. Descripción del proyecto.
2. Problema que resuelve.
3. Objetivos y funcionalidades.
4. Arquitectura del sistema.
5. Tecnologías utilizadas.
6. Modelo entidad-relación.
7. Instalación y configuración.
8. Ejecución del proyecto.
9. Ejecución de tests.
10. Documentación de API.
11. Equipo de desarrollo.
12. Metodología de trabajo.
13. Roadmap y estado del proyecto.

---

## 1. Descripción del proyecto.

## 2. Problema que resuelve.

## 3. Objetivos y funcionalidades.

## 4. Arquitectura del sistema.

## 5. Tecnologías utilizadas.

## 6. Modelo entidad-relación.

## 7. Instalación y configuración.
### Estructura
```text
.github/                 CI, plantillas de Issues y PR
docs/                    Arquitectura, API, datos, workflow y ADRs
migrations/               Migraciones versionadas
scripts/                  Utilidades reproducibles
src/business_app/
  api/                    Adaptadores HTTP
  application/            Casos de uso
  core/                   Configuración, logging y errores
  domain/                 Entidades y reglas
  repositories/            Contratos de persistencia
  infrastructure/         Implementaciones técnicas
tests/
  unit/
  integration/
```
### Instalación
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
```
Copiar `.env.example` a `.env` y completar solo valores locales. Nunca subir secretos.

## Calidad
```bash
ruff check .
ruff format --check .
pytest
pytest --cov=business_app --cov-report=term-missing
```

## 8. Ejecución del proyecto.

## 9. Ejecución de tests.

## 10. Documentación.
### Documentos principales del proyecto
- [Arquitectura](docs/architecture.md)
- [Base de datos](docs/database.md)
- [API](docs/api.md)
- [Guía de desarrollo](docs/development-guide.md)
- [Testing y TDD](docs/testing.md)
- [Workflow](docs/workflow.md)
- [Retrospectiva](docs/retrospective.md)
- [Decisión tecnológica](docs/decisions/ADR.md)


## 11. Equipo de desarrollo.
| Integrante | GitHub | Responsabilidad |
|---|---|---|
| Yang | ZhouYangYang1519 | Pendiente |
| Marco | marcosadhwani | Pendiente |
| Integrante 3 | Pendiente | Pendiente |
| Jose | josegalindo-aidev | Pendiente |

## 12. Metodología de trabajo.
### Flujo de trabajo
1. Seleccionar una historia priorizada.
2. Crear rama desde `main`.
3. Escribir primero el test (Red).
4. Implementar lo mínimo para pasarlo (Green).
5. Refactorizar y mantener los tests en verde.
6. Ejecutar toda la suite y Ruff.
7. Abrir PR, obtener revisión y pasar CI.
8. Integrar en `main`.

Ramas: `feature/<issue>-<descripcion>`, `fix/...`, `test/...`, `docs/...`.
Commits: Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `chore:`).
## 13. Roadmap y estado del proyecto.