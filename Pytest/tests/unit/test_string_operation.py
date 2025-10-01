import pytest


class TestStringOperations:
"""Test cases for string operations"""

@pytest.fixture
def sample_string(self):
return "Hello, Pytest!"

def test_string_length(self, sample_string):
"""Test string length"""
assert len(sample_string) == 14

def test_string_upper(self, sample_string):
"""Test string uppercase conversion"""
assert sample_string.upper() == "HELLO, PYTEST!"

def test_string_split(self, sample_string):
"""Test string splitting"""
parts = sample_string.split(", ")
assert parts == ["Hello", "Pytest!"]

@pytest.mark.parametrize("input_str,expected", [
("hello", "HELLO"),
("WORLD", "WORLD"),
("PyTest", "PYTEST"),
])
def test_multiple_strings_upper(self, input_str, expected):
"""Test multiple strings uppercase conversion"""
assert input_str.upper() == expected
