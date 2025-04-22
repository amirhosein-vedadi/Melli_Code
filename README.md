# Melli Code - Iranian National Code (Python)

[![PyPI version](https://badge.fury.io/py/melli-code.svg)](https://badge.fury.io/py/melli-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/melli-code.svg)](https://pypi.org/project/melli-code/)

Python library to validate and generate Iranian National Codes (کد ملی ایران).

This is a Python port and enhancement of the original JavaScript library [majidh1/iranianNationalCode](https://github.com/majidh1/iranianNationalCode).

## Features

* **Validation**: Check if a given 10-digit string is a valid Iranian National Code (`is_valid`, `validate`).
* **Generation**: Generate random, valid Iranian National Codes (`generate`).
* Pure Python, no runtime dependencies.
* Type-hinted and tested.

## Installation

```bash
pip install melli-code
```

## Usage

### Validation

Use `is_valid` for a boolean check, or `validate` to raise `InvalidNationalCode` on failure.

```python
from melli_code import is_valid, validate, InvalidNationalCode

# Using is_valid (returns True/False)
code1 = "0012345679"  # Valid
code2 = "0012345678"  # Invalid checksum
code3 = "1111111111"  # Invalid (all same digits)
code4 = "12345"       # Invalid format

print(f"'{code1}' is valid: {is_valid(code1)}")
print(f"'{code2}' is valid: {is_valid(code2)}")
print(f"'{code3}' is valid: {is_valid(code3)}")
print(f"'{code4}' is valid: {is_valid(code4)}")

# Using validate (raises exception on failure)
try:
    validate(code1)
    print(f"'{code1}' validation passed!")
except InvalidNationalCode as e:
    print(f"Validation failed for '{code1}': {e}")

try:
    validate(code2)
    print(f"'{code2}' validation passed!")
except InvalidNationalCode as e:
    print(f"Validation failed for '{code2}': {e}") # Expected output

try:
    validate(code4)
    print(f"'{code4}' validation passed!")
except InvalidNationalCode as e:
    print(f"Validation failed for '{code4}': {e}") # Expected output
```

### Generation

Generate a new, random, valid code.

```python
from melli_code import generate

new_code = generate()
print(f"Generated valid code: {new_code}")
# Example Output: Generated valid code: 4848948377 (will vary)
```

## Algorithm Reference

<img style="max-width:80%" src="https://raw.githubusercontent.com/majidh1/iranianNationalCode/master/sakhtare-codemeli.jpg" alt="Structure of Iranian National Code">
<br />
<img style="max-width:80%" src="https://raw.githubusercontent.com/majidh1/iranianNationalCode/master/algorithm-codemeli.jpeg" alt="Algorithm for Iranian National Code">

(Images from the original JavaScript repository)

## Development

1. Clone the repository:
```bash
git clone https://github.com/amirhosein-vedadi/Melli_Code.git
cd melli-code-py
```

2. Create virtual env:
```bash
python -m venv venv
```

3. Activate:
   - Linux/macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`

4. Install editable with dev deps:
```bash
pip install -e .[dev]
```

5. Run tests:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

* Based on the original JavaScript code by [Majid Hooshiyar](https://github.com/majidh1/iranianNationalCode).