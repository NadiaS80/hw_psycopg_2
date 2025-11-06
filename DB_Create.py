import psycopg2
from DB_Settings import Settings

class Create(Settings):

    def create_table_Client(self):
        with self._cursor() as cur:
            cur.execute("""
            create table if not exists Client(
            id serial primary key,
            first_name varchar(80) not null,
            last_name varchar(80) not null,
            email varchar(200) not null unique
            );
            """)
            self._commit()


    def create_table_Phone(self):
        with self._cursor() as cur:
            cur.execute("""
            create table if not exists Phone(
            id serial primary key,
            number varchar(20) not null unique,
            client_id integer not null references Client(id) on delete cascade
            );
            """)
            self._commit()
