import psycopg2


class Settings:

    def __init__(self, database: str, user: str, password: str):
        self.conn = psycopg2.connect(database=database, user=user, password=password)
        
    def _cursor(self):
        return self.conn.cursor()

    def _commit(self):
        self.conn.commit()

    def _close(self):
        self.conn.close()