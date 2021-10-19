# EPAi4 Session4 : Numerical Types

## Qualean

This assignment is about implementing the **Qualean class**. The word Qualean derived  from both **Quantum** and **Boolean**.

### About Qualean

* It can have only  3 **real** states: **True, False, Maybe**. They are represented as **1, 0, -1** respectively.
* When a real state is assigned to Qualean, it **internally picks an imaginary state**.
* The following rule is followed to determine the internal state.
  * Pick a number from distribution **random.uniform(-1, 1)**.
  * Multiply that random number with the **real state**.
  * Round that number using **Banker's rounding method to 10 decimal places**.

### Overview of Implemented Methods

* **Constructor**

  * __init__

    >  Argument: Default state

    Sets the internal state.

  * **gen_internal_state**

    > Arguments: value
    >
    > Returns: Decimal

    Uses random.uniform() distribution to generate the imaginary state.

    With the local context, sets the rounding option to ROUND_HALF_EVEN for bankers rouding method.

* **Utility Methods**

  * **get_with_precision**

    > Argument: value
    >
    > Returns: Decimal

    Get the decimal with appropriate precision and rounding for a given input number.

  * **get_with_precision_from_float**

    > Argument: float
    >
    > Returns: Decimal

    Get the decimal with appripriate precision and rounding for a given float number.

* **Print and Debugging Utilities**

  * __repr__

    > Returns: string

    Returns the representation of the class in string format.

  * __str__

    > Returns: string

    Returns the representation of the class in string format. Used for debugging.

* **Unary Operations**

  * __pos__

  * __neg__

  * __int__

  * __bool__

  * __float__

    > Returns: Decimal

    These unary functions returns the decimal value with the appropriate operations - positive, negative, integer, boolean and float respectively.

* **Comparison Operations**

  * __lt__

  * __le__

  * __eq__

  * __gt__

  * __ge__

    > Arguments: other
    >
    > Returns: bool

    These comparison functions returns boolean value by performing the appropriate comparison operations- less than, less than or equal to, equal to, greater than and, greater than or equal to respectively.

* **Logical Operations**

  * __and__

  * __or__

    > Arguments: other
    >
    > Returns: bool

    These logical functions returns boolean value by performing the logical operations- **and** and **or** respectively.

* **Math operations**

  * __abs__

    > Returns: int

    This function returns the absolute value.

  * __trunc__

    > Returns: int

    This function returns the value after truncation.

  * __invertsign__

    > Returns: float

    This function returns the float value after inverting the sign of existing value.

  * __sqrt__

    > Returns: Decimal

    This function returns the decimal value after performing the square-root operations. In the case of negative numbers - it returns the string with **i** appended to the square-root of the positive value.

* **Binary Operations**

  * __add__

  * __sub__

  * __mul__

    > Argument: other
    >
    > Returns: float

    These binary operations returns the float value after performing binary operations - addition, subtraction, and multiplication respectively.

### Overview Of Tests

| Testcase Name                                           | Description                                                  |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| test_readme_exists                                      | Checks whether the README.md file exists.                    |
| test_readme_contents                                    | Checks whether the README file is descriptive enough with atleast 500 words. |
| test_readme_proper_description                          | Checks whether the class is well defined with many important functions. |
| test_readme_file_for_formatting                         | Checks whether the file is enough header informations.       |
| test_indentations                                       | Checks whether the file is followed the proper indentation. Note that 4 space indentation should be followed for PEP8 guidelines. |
| test_function_name_had_cap_letter                       | Checks whether the function has any uppercase letters.       |
| test_qualean_repr                                       | Verifies the __repr__ implementation.                        |
| test_qualean_str                                        | Verifies the __str__ implementation.                         |
| test_function_qualean_type                              | Checks whether qualean is a class type.                      |
| test_qualean_decimal_precision                          | Checks whether the rounding to 10 decimal precision is happening or not. |
| test_function_count                                     | Checks whether atleast 26 functions are defined for the Qualean class. |
| test_function_repeatations                              | Checks whether any method is repeated.                       |
| test_100_qualeans                                       | To verify the 100 times qualean succeeded or not.            |
| test_function_sqrt                                      | Checks the square root method and also verifies whether the returned value is with proper precision. |
| test_million_qualeans_sum                               | Tests the sum for a million qualeans.                        |
| test_million_qualeans_mul                               | Tests the total of  multiplications of million qualeans.     |
| test_qualean_valid_input                                | Checks whether constructor handles different values for qualean. |
| test_invalid_input_valueerror_provides_relevant_message | Checks the errors message from the constructor for an invalid value. |
| test_qualean_validity                                   | Checks qualean __float__ method.                             |
| test_function_and                                       | Checks qualean __and__ operation.                            |
| test_and_q_notdefined                                   | Checks whether the __and__ operation can handle None value.  |
| test_and_q_false                                        | Checks the __and__ operation.                                |
| test_function_or                                        | Verifies the logical __or__ operation for the qualeans.      |
| test_or_q_notdefined                                    | Verfifies the logical __or__ operation with None value.      |
| test_or_q_false                                         | Verifies the logical __or__ operation with false value.      |
| test_function_add                                       | Checks the implementation of __add__ for two qualeans.       |
| test_function_add_non_qualean                           | Checks the addition of an qualean with float value.          |
| test_function_mul                                       | Checks the multiplication of two qualeans.                   |
| test_function_mul_non_qualean                           | Checks the multiplication of an qualean with float value.    |
| test_function_ge                                        | Checks the comparison operation greater than or equal to.    |
| test_function_ge_non_qualean                            | Compare qualean with non-qualean for comparison operator greater than or equal to. |
| test_function_gt                                        | Checks the greater than operation.                           |
| test_function_gt_non_qualean                            | Compares the qualean with non-qualean for greater than operation. |
| test_function_le                                        | Checks the comparison operation less than or equal to.       |
| test_function_le_non_qualean                            | Compares the qualean with non-qualean for less than or equal to operation. |
| test_function_lt                                        | Checks the comparison operation less than.                   |
| test_function_lt_non_qualean                            | Compares the qualean with non-qualean for less than operation. |
| test_function_with_non_number                           | Checks the comparison operations with string type.           |
| test_function_bool                                      | Checks the __bool__ method.                                  |
| test_function_eq                                        | Checks the equality of two qualeans.                         |
| test_function_float                                     | Checks the __float__ conversion.                             |
| test_function_invertsign                                | Checks the invertsign method.                                |



### Local Results

```text
collected 42 items                                                                                                   

test_readme_exists PASSED                                                                    [  2%]
test_readme_contents PASSED                                                                  [  4%]
test_readme_proper_description PASSED                                                        [  7%]
test_readme_file_for_formatting PASSED                                                       [  9%]
test_indentations PASSED                                                                     [ 11%]
test_function_name_had_cap_letter PASSED                                                     [ 14%]
test_qualean_repr PASSED                                                                     [ 16%]
test_qualean_str PASSED                                                                      [ 19%]
test_function_qualean_type PASSED                                                            [ 21%]
test_qualean_decimal_precision PASSED                                                        [ 23%]
test_function_count PASSED                                                                   [ 26%]
test_function_repeatations PASSED                                                            [ 28%]
test_100_qualeans PASSED                                                                     [ 30%]
test_function_sqrt PASSED                                                                    [ 33%]
test_million_qualeans_sum PASSED                                                             [ 35%]
test_million_qualeans_mul PASSED                                                             [ 38%]
test_qualean_valid_input PASSED                                                              [ 40%]
test_invalid_input_valueerror_provides_relevant_message PASSED                               [ 42%]
test_qualean_validity PASSED                                                                 [ 45%]
test_function_and PASSED                                                                     [ 47%]
test_and_q_notdefined PASSED                                                                 [ 50%]
test_and_q_false PASSED                                                                      [ 52%]
test_function_or PASSED                                                                      [ 54%]
test_or_q_notdefined PASSED                                                                  [ 57%]
test_or_q_false PASSED                                                                       [ 59%]
test_function_add PASSED                                                                     [ 61%]
test_function_add_non_qualean PASSED                                                         [ 64%]
test_function_mul PASSED                                                                     [ 66%]
test_function_mul_non_qualean PASSED                                                         [ 69%]
test_function_ge PASSED                                                                      [ 71%]
test_function_ge_non_qualean PASSED                                                          [ 73%]
test_function_gt PASSED                                                                      [ 76%]
test_function_gt_non_qualean PASSED                                                          [ 78%]
test_function_le PASSED                                                                      [ 80%]
test_function_le_non_qualean PASSED                                                          [ 83%]
test_function_lt PASSED                                                                      [ 85%]
test_function_lt_non_qualean PASSED                                                          [ 88%]
test_function_with_non_number PASSED                                                         [ 90%]
test_function_bool PASSED                                                                    [ 92%]
test_function_eq PASSED                                                                      [ 95%]
test_function_float PASSED                                                                   [ 97%]
test_function_invertsign PASSED                                                              [100%]

========================== 42 passed in 10.61 seconds =============================================
```



