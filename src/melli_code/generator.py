# src/melli_code/generator.py
import random
from .validator import is_valid # Relative import

def generate() -> str:
    """
    Generates a valid Iranian National Code (Melli Code).

    Ensures the generated code is not composed of all the same digits
    and passes the validation checksum.

    Returns:
        A 10-digit valid national code string.
    """
    while True:
        # Generate the first 9 digits randomly
        first_9_digits = [random.randint(0, 9) for _ in range(9)]

        # Avoid generating all same digits for the first 9 (optional optimization)
        # if len(set(first_9_digits)) == 1:
        #     continue # Try again immediately if first 9 are same

        # Calculate the weighted sum
        weighted_sum = sum(digit * weight for digit, weight in zip(first_9_digits, range(10, 1, -1)))
        remainder = weighted_sum % 11

        # Determine the check digit
        if remainder < 2:
            check_digit = remainder
        else:
            check_digit = 11 - remainder

        # Combine into the full code
        code_list = first_9_digits + [check_digit]
        code_str = "".join(map(str, code_list))

        # Validate the generated code using our own validator
        # This implicitly checks for all-same-digits as well.
        if is_valid(code_str):
            return code_str
        # Loop again if generated code is invalid (e.g., ended up being all 0s)