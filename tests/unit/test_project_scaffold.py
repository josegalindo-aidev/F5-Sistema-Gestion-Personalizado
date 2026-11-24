from business_app.core.exceptions import (
    ApplicationError,
    BusinessRuleError,
    ResourceNotFoundError,
)


def test_application_exceptions_share_common_base():
    assert issubclass(ResourceNotFoundError, ApplicationError)
    assert issubclass(BusinessRuleError, ApplicationError)
