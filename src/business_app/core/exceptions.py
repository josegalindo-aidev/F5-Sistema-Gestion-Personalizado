class ApplicationError(Exception):
    """Base de excepciones controladas de la aplicación."""


class ResourceNotFoundError(ApplicationError):
    """El recurso solicitado no existe."""


class BusinessRuleError(ApplicationError):
    """Una regla de negocio impide completar la operación."""
