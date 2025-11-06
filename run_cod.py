import psycopg2
from DB_Settings import Settings
from DB_Create import Create
from DB_Control import DB_Control

database = 'YOUR_DB_NAME'
password = 'YOUR_PASSWORD'

if __name__ == '__main__':

    creator = Create(database=database, user='postgres', password=password)
    creator.create_table_Client()
    creator.create_table_Phone()
    client_1 = DB_Control(database=database, user='postgres', password=password)
    client_2 = DB_Control(database=database, user='postgres', password=password)
    client_1_id = client_1.insert_Client('Pavel', 'Durov', 'love_it_tg@mail.ru')
    client_2_id = client_2.insert_Client('Guido', 'van Rossum', 'guido.vr@pythonlabs.org')
    client_1.insert_Phone('+7 999 000 77 89', client_1_id)
    client_1.insert_Phone('+971 7 2013 0420', client_1_id)
    client_2.insert_Phone('+31 6 1991 1020', client_2_id)
    client_1.update_Client(client_1_id, email = '0xblueplane@telegram.org')
    client_1.delete_Phone(client_1_id, '+7 999 000 77 89')
    client_1.delete_Client(client_1_id)
    print(client_2.find_Client(last_name='van Rossum'))