import pytest
import logging
from typing import Dict, Any
import json
import os


# Fixture for logging
@pytest.fixture(scope="session")
def logger():
"""Setup logging for tests"""
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
return logging.getLogger(__name__)


# Fixture for test configuration
@pytest.fixture(scope="session")
def config():
"""Load test configuration"""
config = {
"base_url": "https://jsonplaceholder.typicode.com",
"timeout": 30,
"test_data": {
"valid_user_id": 1,
"invalid_user_id": 99999
}
}
return config


# Fixture for test data
@pytest.fixture
def test_data():
"""Provide test data"""
return {
"numbers": [1, 2, 3, 4, 5],
"strings": ["hello", "world", "pytest"],
"user_data": {
"name": "John Doe",
"email": "john@example.com",
"age": 30
}
}


# Autouse fixture for test setup
@pytest.fixture(autouse=True)
def setup_teardown():
"""Setup and teardown for each test"""
# Setup
print("\n=== Starting test ===")

yield

# Teardown
print("=== Test completed ===\n")


# Fixture with finalizer
@pytest.fixture
def temporary_file():
"""Create a temporary file for testing"""
file_path = "temp_test_file.txt"
with open(file_path, 'w') as f:
f.write("Test data")

yield file_path

# Cleanup
if os.path.exists(file_path):
os.remove(file_path)


# Session-scoped fixture
@pytest.fixture(scope="session")
def database_connection():
"""Simulate database connection"""
print("Setting up database connection")
connection = {"connected": True, "db": "test_db"}

yield connection

print("Closing database connection")
connection["connected"] = False


# Hook for test failure handling
def pytest_runtest_makereport(item, call):
"""Custom reporting for test failures"""
if call.when == "call" and call.excinfo is not None:
print(f"\n❌ Test {item.name} FAILED!")
print(f"Error: {call.excinfo.value}")


# Custom marker validation
def pytest_configure(config):
"""Register custom markers"""
config.addinivalue_line(
"markers", "smoke: mark test as smoke test"
)
config.addinivalue_line(
"markers", "regression: mark test as regression test"
)
