import unittest
import psycopg2
import os

class TestPostgresConnection(unittest.TestCase):
    def setUp(self):
        """
        Set up the PostgreSQL connection before each test.
        """
        self.connection = psycopg2.connect(
            host=os.getenv("PGHOST"),
            port=os.getenv("PGPORT"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            dbname=os.getenv("PGDATABASE")
        )
        self.cursor = self.connection.cursor()

    def tearDown(self):
        """
        Close the PostgreSQL connection after each test.
        """
        self.cursor.close()
        self.connection.close()

    def test_connection(self):
        """
        Test if the connection to the PostgreSQL database is successful.
        """
        self.cursor.execute("SELECT 1;")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 1, "Database connection test failed.")

    def test_sample_query(self):
        """
        Test a sample query on the database.
        """
        self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = self.cursor.fetchall()
        print("Tables in the database:", tables)
        self.assertIsNotNone(tables, "No tables found in the database.")

    def test_insert_and_retrieve_data(self):
        """
        Test inserting and retrieving data from a test table.
        """
        self.cursor.execute("CREATE TEMP TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));")
        self.cursor.execute("INSERT INTO test_table (name) VALUES ('Test Name');")
        self.connection.commit()

        self.cursor.execute("SELECT name FROM test_table WHERE name = 'Test Name';")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'Test Name', "Data insertion or retrieval failed.")

    def test_update_data(self):
        """
        Test updating data in a test table.
        """
        self.cursor.execute("CREATE TEMP TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));")
        self.cursor.execute("INSERT INTO test_table (name) VALUES ('Old Name');")
        self.connection.commit()

        self.cursor.execute("UPDATE test_table SET name = 'New Name' WHERE name = 'Old Name';")
        self.connection.commit()

        self.cursor.execute("SELECT name FROM test_table WHERE name = 'New Name';")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'New Name', "Data update failed.")

    def test_delete_data(self):
        """
        Test deleting data from a test table.
        """
        self.cursor.execute("CREATE TEMP TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));")
        self.cursor.execute("INSERT INTO test_table (name) VALUES ('Delete Me');")
        self.connection.commit()

        self.cursor.execute("DELETE FROM test_table WHERE name = 'Delete Me';")
        self.connection.commit()

        self.cursor.execute("SELECT name FROM test_table WHERE name = 'Delete Me';")
        result = self.cursor.fetchone()
        self.assertIsNone(result, "Data deletion failed.")

if __name__ == "__main__":
    unittest.main()
