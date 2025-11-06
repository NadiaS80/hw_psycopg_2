import psycopg2
from DB_Settings import Settings

class DB_Control(Settings):

    def insert_Client(self, first_name: str, last_name: str, email: str):
        """Insert a new client into the database.

        Args:
            first_name (str): Client's first name.
            last_name (str): Client's last name.
            email (str): Client's email address.

        Returns:
            int: The ID of the newly created client.
        """
        with self._cursor() as cur:
            cur.execute("""
            insert into Client(first_name, last_name, email)
            values (%s, %s, %s)
            returning id;
            """, (first_name, last_name, email))
            client_id = cur.fetchone()[0]
            self._commit()
            return client_id


    def insert_Phone(self, number: str, client_id: int):
        """Insert a new phone number for an existing client.

        Args:
            number (str): Phone number to add.
            client_id (int): ID of the associated client.
        """
        with self._cursor() as cur:
            cur.execute("""
            insert into Phone(number, client_id)
            values (%s, %s);
            """, (number, client_id))
            self._commit()


    def update_Client(self, id, first_name = None, last_name = None, email = None):
        """Update client information by ID.

        Args:
            id (int): Client ID.
            first_name (str, optional): New first name.
            last_name (str, optional): New last name.
            email (str, optional): New email address.
        """
        with self._cursor() as cur:
            for obj, value in {'first_name': first_name, 'last_name': last_name, 'email': email}.items():
                if value is not None:
                    cur.execute(f"""
                    update Client set {obj} = %s
                    where id = %s;
                    """, (value, id))
            self._commit()


    def delete_Phone(self, client_id, number):
        """Delete a specific phone number for a given client.

        Args:
            client_id (int): Client ID.
            number (str): Phone number to delete.
        """
        with self._cursor() as cur:
            cur.execute("""
            delete from Phone 
            where client_id = %s and number = %s;
            """, (client_id, number))
            self._commit()


    def delete_Client(self, id):
        """Delete a client and all related phone numbers.

        Args:
            id (int): Client ID.
        """
        with self._cursor() as cur:
            cur.execute("""
            delete from Client 
            where id = %s;
            """, (id,))
            self._commit()


    def find_Client(self, first_name = None, last_name = None, email = None, number = None):
        """Find a client by first name, last name, email, or phone number.

        Args:
            first_name (str, optional): Filter by first name.
            last_name (str, optional): Filter by last name.
            email (str, optional): Filter by email.
            number (str, optional): Filter by phone number.

        Returns:
            dict | None: A dictionary with client data, or None if not found.
        """
        client_info = {}
        data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'number': number}
        values = []
        queries = []
        for key, value in data.items():
            if value is not None:
                queries.append(f'{key} = %s')
                values.append(value)
        if queries:
            select = f"""
            select c.id, c.first_name, c.last_name, c.email, p.number from Client c 
            left join Phone p on c.id = p.client_id 
            where {' and '.join(queries)}
            """
            with self._cursor() as cur:
                cur.execute(select, tuple(values))
                info = cur.fetchall()
                client_info['id'] = info[0][0] 
                client_info['first_name'] = info[0][1] 
                client_info['last_name'] = info[0][2] 
                client_info['email'] = info[0][3] 
                client_info['numbers'] = [i[4] for i in info if i[4] is not None]
        return client_info if client_info else None