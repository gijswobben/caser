from enum import Enum, auto


class Case(Enum):
    """Different ways of writing strings."""

    SNAKE_CASE = auto()
    """Example: snake_case"""
    PASCAL_CASE = auto()
    """Example: PascalCase"""
    KEBAB_CASE = auto()
    """Example: kebab-case"""
    CAMEL_CASE = auto()
    """Example: camelCase"""
    SPACE_CASE = auto()
    """Example: space case"""


LOGGER_NAME = "caser"
