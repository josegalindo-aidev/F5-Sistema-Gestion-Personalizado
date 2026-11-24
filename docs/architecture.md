# Arquitectura

## Principio
Separar reglas de negocio de los detalles técnicos. La dirección de dependencias apunta hacia el dominio.

| Capa | Responsabilidad |
|---|---|
| API | HTTP, rutas, serialización y códigos de estado |
| Application | Casos de uso y coordinación |
| Domain | Entidades, invariantes y reglas |
| Repositories | Contratos de persistencia |
| Infrastructure | ORM, conexión SQL y adaptadores |

No colocar reglas de negocio complejas en controladores ni SQL directo en servicios. Crear módulos funcionales cuando se conozca el dominio; evitar carpetas vacías por anticipado.
