API
======
Documentation for the different methods available in `caser`.


Automatic conversions
----------------------------
This section contains methods that can be used to convert strings into a different case automatically (without specifying the source style used).

.. note:: Automatic conversions detect the current case first and use that to convert to snake case. From snake case it will convert into the desired style. This method reduces the size of this library and reduces complexity.

.. autofunction:: caser.to_camel_case
.. autofunction:: caser.to_kebab_case
.. autofunction:: caser.to_pascal_case
.. autofunction:: caser.to_snake_case
.. autofunction:: caser.to_space_case


Specific conversions
----------------------------
This section contains methods to convert one style into another.

.. note:: It is better to use the automatic conversions above. The automatic conversions will first detect the style of the string, convert it into snake case, and then from snake case into the desired format.

.. autofunction:: caser.camel_to_snake_case
.. autofunction:: caser.kebab_to_snake_case
.. autofunction:: caser.pascal_to_snake_case
.. autofunction:: caser.snake_to_camel_case
.. autofunction:: caser.snake_to_kebab_case
.. autofunction:: caser.snake_to_pascal_case
.. autofunction:: caser.snake_to_space_case
.. autofunction:: caser.space_to_snake_case


Utils
----------------------------
Utility functions that can be used directly as well.

.. autofunction:: caser.detect_case


Constants
----------------------------

.. autoclass:: caser.constants.Case
   :members:


Exceptions
----------------------------

.. automodule:: caser.exceptions
   :members:
