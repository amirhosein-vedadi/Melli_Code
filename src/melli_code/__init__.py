# src/melli_code/__init__.py
"""
Melli Code: Iranian National Code Validator and Generator.

Provides functions to validate existing codes and generate new valid codes
according to the official algorithm. Package name: melli-code.
"""
__version__ = "1.0.1" # <--- Set initial version

from .validator import is_valid, validate
from .generator import generate
from .exceptions import InvalidNationalCode

# Controls what 'from melli_code import *' imports
__all__ = [
    'is_valid',
    'validate',
    'generate',
    'InvalidNationalCode',
    '__version__'
]