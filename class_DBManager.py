import psycopg2

import os

class DBManager():

    def __init__(self):
        """Конструктор класса"""
        self.conn_database = 'CorseTest'
        self.conn_password = str(os.getenv('PSQL_KEY'))


    def insert_employer(self, temp_dict):
        """Записывает информацию о компании в БД"""
        with psycopg2.connect(host = 'localhost',
        database = self.conn_database,
        user = 'postgres',
        password = self.conn_password) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO employees VALUES (%s,%s,%s)", (temp_dict['id_employer'],
                                                                         temp_dict['employer_name'],
                                                                         temp_dict['industries']))
                cur.execute("SELECT * FROM employees")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
        conn.close()