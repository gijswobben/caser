import logging
import re

from caser.constants import LOGGER_NAME, Case
from caser.exceptions import NoCaseDetectedException

logger = logging.getLogger(LOGGER_NAME)


def pascal_to_snake_case(string: str) -> str:
    """Convert PascalCase to snake_case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    output = ""
    for i in range(len(string) - 1):
        if string[i].isupper() and not string[i + 1].isupper():
            output = output + "_"
        output = output + string[i]
    output = output + string[-1]
    return output.lower().strip("_")


def camel_to_snake_case(string: str) -> str:
    """Convert camelCase to snake_case case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    return pascal_to_snake_case(string)


def kebab_to_snake_case(string: str) -> str:
    """Convert kebab-case to snake_case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    output = string.replace("-", "_")
    return output.lower()


def space_to_snake_case(string: str) -> str:
    """Convert "space case" to snake_case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    output = string.replace(" ", "_").lower()
    return output


def snake_to_pascal_case(string: str) -> str:
    """Convert snake_case to PascalCase.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    for i in range(len(string) - 1):
        if string[i] == "_":
            string = string[: i + 1] + string[i + 1].upper() + string[i + 2 :]
    string = string[0].upper() + string[1:]
    return string.replace("_", "")


def snake_to_camel_case(string: str) -> str:
    """Convert snake_case to camelCase.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    for i in range(len(string) - 1):
        if string[i] == "_":
            string = string[: i + 1] + string[i + 1].upper() + string[i + 2 :]
    return string.replace("_", "")


def snake_to_kebab_case(string: str) -> str:
    """Convert snake_case to kebab-case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    output = string.replace("_", "-").strip("-")
    return output


def snake_to_space_case(string: str) -> str:
    """Convert snake_case to "space case".

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    output = string.replace("_", " ")
    return output


_mapping = {
    Case.CAMEL_CASE: camel_to_snake_case,
    Case.PASCAL_CASE: pascal_to_snake_case,
    Case.KEBAB_CASE: kebab_to_snake_case,
    Case.SNAKE_CASE: lambda x: x,
    Case.SPACE_CASE: space_to_snake_case,
}

PASCAL_CASE_REGEX = (
    r"^[A-Z]([A-Z0-9]*[a-z][a-z0-9]*[A-Z]|[a-z0-9]*[A-Z][A-Z0-9]*[a-z])[A-Za-z0-9]*$"
)
CAMEL_CASE_REGEX = (
    r"^[a-z]([A-Z0-9]*[a-z][a-z0-9]*[A-Z]|[a-z0-9]*[A-Z][A-Z0-9]*[a-z])[A-Za-z0-9]*$"
)
SNAKE_CASE_REGEX = r"^([a-zA-Z0-9]+_|[a-zA-Z0-9]+)*$"
KEBAB_CASE_REGEX = r"^([a-zA-Z0-9]+-|[a-zA-Z0-9]+)*$"
SPACE_CASE_REGEX = r"^([a-zA-Z0-9]+\s|[a-zA-Z0-9]+)*$"


def detect_case(string: str) -> Case:
    """Detect the case that a string was written in.

    Args:
        string (str): The string to detect.

    Raises:
        NoCaseDetectedException: When no case could be detected or the
            string has ambiguous case.

    Returns:
        Case: The :class:`Case <caser.constants.Case>` that matches the string.
    """

    if re.match(PASCAL_CASE_REGEX, string):
        return Case.PASCAL_CASE
    elif re.match(CAMEL_CASE_REGEX, string):
        return Case.CAMEL_CASE
    elif re.match(SNAKE_CASE_REGEX, string):
        return Case.SNAKE_CASE
    elif re.match(KEBAB_CASE_REGEX, string):
        return Case.KEBAB_CASE
    elif re.match(SPACE_CASE_REGEX, string):
        return Case.SPACE_CASE
    else:
        raise NoCaseDetectedException(f'Unable to detect case in string: "{string}"')


def to_pascal_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to PascalCase.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    detected_case = detect_case(string)
    snake_case = _mapping[detected_case](string)
    return snake_to_pascal_case(snake_case).replace(" ", "")


def to_camel_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to camelCase.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    detected_case = detect_case(string)
    snake_case = _mapping[detected_case](string)
    return snake_to_camel_case(snake_case).replace(" ", "")


def to_snake_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to snake_case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    detected_case = detect_case(string)
    return _mapping[detected_case](string).replace(" ", "")


def to_kebab_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to kebab-case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    detected_case = detect_case(string)
    snake_case = _mapping[detected_case](string)
    return snake_to_kebab_case(snake_case).replace(" ", "")


def to_space_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to space case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    detected_case = detect_case(string)
    snake_case = _mapping[detected_case](string)
    return snake_to_space_case(snake_case)


def to_upper_snake_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to snake_case in upper case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    return to_snake_case(string).upper()


def to_upper_kebab_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to kebab-case in upper case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    return to_kebab_case(string).upper()


def to_upper_space_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to "space case" in upper case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    return to_space_case(string).upper()


def to_lower_snake_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to snake_case in lower case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    return to_snake_case(string).lower()


def to_lower_kebab_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to kebab-case in lower case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    return to_kebab_case(string).lower()


def to_lower_space_case(string: str) -> str:
    """Detect the current case of the string and convert automatically
    to "space case" in lower case.

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.
    """

    return to_space_case(string).lower()
