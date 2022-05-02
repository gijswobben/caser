# Caser
Caser is a library that automatically converts strings from one case style to another.

## Installation
Run:

```shell
pip install caser
```

## Basic use
Caser can automatically detect the case style so it's enough to call a destination style like this:

```python
>>> from caser import to_snake_case
>>> my_string = "Hello There"
>>> print(to_snake_case(my_string))
hello_there
```

## Available styles

Available styles are:

- snake_case
- kebab-case
- PascalCase
- camelCase
- space case
