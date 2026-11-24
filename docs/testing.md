# Testing y TDD

## Ciclo
1. Red: escribir una prueba que falle por la razón esperada.
2. Green: implementar el mínimo código para pasarla.
3. Refactor: mejorar el diseño sin alterar el comportamiento.

| Tipo | Alcance |
|---|---|
| Unitarias | Dominio y casos de uso |
| Integración | Repositorios, ORM y base de datos |
| API | Contrato HTTP y validaciones |

Comandos: `pytest`, `pytest -m unit`, `pytest -m integration` y `pytest --cov=business_app`.

Cobertura mínima inicial configurada al 70%; no sustituye la calidad de los casos de prueba.
