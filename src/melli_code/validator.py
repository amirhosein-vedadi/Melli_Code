# src/melli_code/validator.py
import re
from .exceptions import InvalidNationalCode # Relative import

def is_valid(code: str) -> bool:
    """
    Validates an Iranian National Code (Melli Code).

    Args:
        code: The 10-digit national code string.

    Returns:
        True if the code is valid, False otherwise (including format errors).
    """
    if not isinstance(code, str) or not re.match(r'^\d{10}$', code):
        return False

    # Check for codes with all same digits (invalid)
    if len(set(code)) == 1:
        return False

    check_digit = int(code[9])
    try:
        weighted_sum = sum(int(digit) * weight for digit, weight in zip(code[:9], range(10, 1, -1)))
    except ValueError: # Should not happen if regex matched, but safe practice
         return False

    remainder = weighted_sum % 11

    if remainder < 2:
        return check_digit == remainder
    else:
        return check_digit == 11 - remainder

def validate(code: str) -> None:
    """
    Validates an Iranian National Code (Melli Code). Raises an exception if invalid.

    Args:
        code: The 10-digit national code string.

    Raises:
        InvalidNationalCode: If the code format is incorrect or the checksum fails.
    """
    # Reuse is_valid but provide a specific error message
    if not isinstance(code, str) or not re.match(r'^\d{10}$', code):
         raise InvalidNationalCode(f"Invalid format: Input '{code}' must be a 10-digit string.")
    if len(set(code)) == 1:
         raise InvalidNationalCode(f"Invalid code: '{code}' consists of all identical digits.")

    if not is_valid(code):
        # If format is okay and not all same digits, the only reason left is checksum
        raise InvalidNationalCode(f"Invalid checksum for code '{code}'.")
    # If we reach here, the code is valid.