import psycopg2


class Settings:

    def __init__(self, database: str, user: str, password: str):
        """Initialize database connection.

        Args:
            database (str): Name of the PostgreSQL database.
            user (str): Database username.
            password (str): Database password.
            self.conn = psycopg2.connect(database=database, user=user, password=password)
        """
        
    def _cursor(self):
        """Create and return a new database cursor."""
        return self.conn.cursor()

    def _commit(self):
        """Commit the current transaction to the database."""
        self.conn.commit()

    def _close(self):
        """Close the database connection."""
        self.conn.close()