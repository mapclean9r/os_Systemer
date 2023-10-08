
import sqlite3
import pytest

# Define your SQLite database connection and cursor.
# You may want to create a separate testing database.
DATABASE = "guid.db"


@pytest.fixture(scope="module")
def setup_database():
    # Set up a temporary database or testing environment.
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create necessary tables and insert sample data.
    cursor.execute(
        "CREATE TABLE users (ID INTEGER PRIMARY 90, FORNAVN TEXT, ETTERNAVN TEXT, AGE )")
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
                   ("testuser", "test@example.com"))

    conn.commit()
    yield conn

    # Teardown the database connection after testing.
    conn.close()
    # Optionally, you can delete the testing database file.


def test_user_data_exists(setup_database):
    conn = setup_database
    cursor = conn.cursor()

    # Query the database to check if user data exists.
    cursor.execute("SELECT * FROM users WHERE username=?", ("testuser",))
    user_data = cursor.fetchone()

    assert user_data is not None, "User data not found in the database"
    assert user_data[1] == "testuser", "Username does not match"


if __name__ == "__main__":
    pytest.main()
