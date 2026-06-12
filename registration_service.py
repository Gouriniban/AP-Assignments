import re


class InvalidEmailError(ValueError):
    """
    Raised when the email is invalid.
    """

    def __init__(self, email):
        message = f"Invalid email address provided: '{email}'"
        super().__init__(message)


class UnderageError(ValueError):
    """
    Raised when the user is under 18 years old.
    """

    def __init__(self, age):
        message = f"User must be at least 18 years old. Provided age: {age}"
        super().__init__(message)


class RegistrationService:
    """
    Service class for user registration validation.
    """

    EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    def register_user(self, email: str, age: int) -> bool:
        """
        Validates email and age before registration.

        Args:
            email (str): User email
            age (int): User age

        Returns:
            bool: True if registration succeeds

        Raises:
            InvalidEmailError
            UnderageError
        """

        # Internal invariant assertion
        assert isinstance(age, int), "Age must be an integer"

        # Check for empty or null email
        if email is None or email.strip() == "":
            raise InvalidEmailError(email)

        # Validate email format
        if not re.match(self.EMAIL_PATTERN, email):
            raise InvalidEmailError(email)

        # Check minimum age requirement
        if age < 18:
            raise UnderageError(age)

        return True