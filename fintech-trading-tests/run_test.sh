#!/bin/bash

# Connect to PostgreSQL database and run test cases using a Python script framework

# Set environment variables for PostgreSQL connection
export PGHOST="your_postgres_host"
export PGPORT="your_postgres_port"
export PGUSER="your_postgres_user"
export PGPASSWORD="your_postgres_password"
export PGDATABASE="your_postgres_database"

# Activate Python virtual environment
source venv/bin/activate

# Run the Python test script
python -m unittest discover -s tests -p "*_test.py"

# Deactivate virtual environment
deactivate
