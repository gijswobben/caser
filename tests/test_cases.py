import pytest

import caser
from caser.constants import Case
from caser.exceptions import NoCaseDetectedException


def test_detect_case():
    case_examples = {
        Case.CAMEL_CASE: [
            "camelCase",
        ],
        Case.PASCAL_CASE: [
            "PascalCase",
        ],
        Case.KEBAB_CASE: [
            "kebab-case",
        ],
        Case.SNAKE_CASE: [
            "snake_case",
        ],
        Case.SPACE_CASE: [
            "space case",
        ],
    }
    for case_enum, examples in case_examples.items():
        for example in examples:
            assert caser.detect_case(example) == case_enum, "Wrong case detected"

    with pytest.raises(NoCaseDetectedException):
        caser.detect_case("this_HasAnIncorrect-case")


def test_conversions():
    functions_mapping = {
        Case.KEBAB_CASE: caser.to_kebab_case,
        Case.PASCAL_CASE: caser.to_pascal_case,
        Case.CAMEL_CASE: caser.to_camel_case,
        Case.SPACE_CASE: caser.to_space_case,
        Case.SNAKE_CASE: caser.to_snake_case,
    }
    conversions = {
        Case.SNAKE_CASE: {
            Case.KEBAB_CASE: ("some-string-here", "some_string_here"),
            Case.PASCAL_CASE: ("SomeStringHere", "some_string_here"),
            Case.CAMEL_CASE: ("someStringHere", "some_string_here"),
            Case.SPACE_CASE: ("some string here", "some_string_here"),
        },
        Case.KEBAB_CASE: {
            Case.PASCAL_CASE: ("SomeStringHere", "some-string-here"),
            Case.CAMEL_CASE: ("someStringHere", "some-string-here"),
            Case.SPACE_CASE: ("some string here", "some-string-here"),
            Case.SNAKE_CASE: ("some_string_here", "some-string-here"),
        },
        Case.PASCAL_CASE: {
            Case.KEBAB_CASE: ("some-string-here", "SomeStringHere"),
            Case.CAMEL_CASE: ("someStringHere", "SomeStringHere"),
            Case.SPACE_CASE: ("some string here", "SomeStringHere"),
            Case.SNAKE_CASE: ("some_string_here", "SomeStringHere"),
        },
        Case.CAMEL_CASE: {
            Case.KEBAB_CASE: ("some-string-here", "someStringHere"),
            Case.PASCAL_CASE: ("SomeStringHere", "someStringHere"),
            Case.SPACE_CASE: ("some string here", "someStringHere"),
            Case.SNAKE_CASE: ("some_string_here", "someStringHere"),
        },
        Case.SPACE_CASE: {
            Case.KEBAB_CASE: ("some-string-here", "some string here"),
            Case.PASCAL_CASE: ("SomeStringHere", "some string here"),
            Case.CAMEL_CASE: ("someStringHere", "some string here"),
            Case.SNAKE_CASE: ("some_string_here", "some string here"),
        },
    }
    for target_case, examples_mapping in conversions.items():
        for original_case, (original_string, target_string) in examples_mapping.items():
            converted_string = functions_mapping[target_case](original_string)
            assert target_string == converted_string, (
                f"Error converting {original_case} with function {functions_mapping[target_case]}. "
                f"Output = {converted_string}, expected {target_string}"
            )

    functions_mapping = {
        Case.KEBAB_CASE: caser.to_lower_kebab_case,
        Case.SPACE_CASE: caser.to_lower_space_case,
        Case.SNAKE_CASE: caser.to_lower_snake_case,
    }

    for target_case, examples_mapping in conversions.items():
        # Skip these because it doesn't make sense to convert them to
        # upper or lower case
        if target_case in [Case.CAMEL_CASE, Case.PASCAL_CASE]:
            continue
        for original_case, (original_string, target_string) in examples_mapping.items():
            converted_string = functions_mapping[target_case](original_string)
            original_string = original_string.upper()
            assert target_string == converted_string, (
                f"Error converting {original_case} with function {functions_mapping[target_case]}. "
                f"Output = {converted_string}, expected {target_string}"
            )

    functions_mapping = {
        Case.KEBAB_CASE: caser.to_upper_kebab_case,
        Case.SPACE_CASE: caser.to_upper_space_case,
        Case.SNAKE_CASE: caser.to_upper_snake_case,
    }

    for target_case, examples_mapping in conversions.items():
        # Skip these because it doesn't make sense to convert them to
        # upper or lower case
        if target_case in [Case.CAMEL_CASE, Case.PASCAL_CASE]:
            continue
        for original_case, (original_string, target_string) in examples_mapping.items():
            converted_string = functions_mapping[target_case](original_string)
            target_string = target_string.upper()
            assert target_string == converted_string, (
                f"Error converting {original_case} with function {functions_mapping[target_case]}. "
                f"Output = {converted_string}, expected {target_string}"
            )
