class VbanCLIError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message: str, code: int = 1):
        super().__init__(message)
        self.code = code


class VbanCLIConnectionError(VbanCLIError):
    """Exception raised for connection errors."""


class VbanCLIValidationError(VbanCLIError):
    """Exception raised for validation errors."""
