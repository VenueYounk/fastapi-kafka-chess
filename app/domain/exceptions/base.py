from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationException(Exception):
    @property
    def message(self):
        return "An application exception occurred"

class EmptyValueException(ApplicationException):
    @property
    def message(self):
        return "Value cannot be empty"