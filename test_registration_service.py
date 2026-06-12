import pytest

from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)


@pytest.fixture
def service():
    """
    Shared fixture for RegistrationService.
    """
    return RegistrationService()


def test_successful_registration(service):
    assert service.register_user("john.doe@example.com", 25) is True


def test_empty_email(service):
    with pytest.raises(InvalidEmailError) as exc_info:
        service.register_user("", 22)

    assert "Invalid email address" in str(exc_info.value)


def test_none_email(service):
    with pytest.raises(InvalidEmailError):
        service.register_user(None, 22)


def test_invalid_email_format(service):
    with pytest.raises(InvalidEmailError):
        service.register_user("invalid-email", 30)


def test_missing_domain(service):
    with pytest.raises(InvalidEmailError):
        service.register_user("user@", 21)


def test_underage_user(service):
    with pytest.raises(UnderageError) as exc_info:
        service.register_user("teen@example.com", 16)

    assert "at least 18 years old" in str(exc_info.value)


def test_boundary_age(service):
    assert service.register_user("adult@example.com", 18) is True