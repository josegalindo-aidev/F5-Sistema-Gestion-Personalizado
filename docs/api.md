# Diseño de API REST

Convenciones propuestas:
- Prefijo `/api/v1`.
- Recursos en plural y nombres consistentes.
- JSON como formato de intercambio.
- Validación de entrada y respuestas documentadas.
- Paginación y filtrado en colecciones.
- Errores homogéneos.

| HTTP | Uso |
|---|---|
| 200 | Operación correcta |
| 201 | Recurso creado |
| 204 | Correcto sin cuerpo |
| 400 | Petición inválida |
| 404 | Recurso inexistente |
| 409 | Conflicto |
| 422 | Datos no válidos, según framework |
| 500 | Error inesperado |

Catálogo de endpoints pendiente de definir el dominio.
