import psycopg2

import os

import self as self


class DBManager():

    def __init__(self):
        """Конструктор класса"""
        self.conn = psycopg2.connect(host = 'localhost',
        database = 'CorseTest',
        user = 'postgres',
        password = str(os.getenv('PSQL_KEY')))



    def insert_employer(self, temp_dict):
        """Записывает информацию о компании в БД"""
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO employers VALUES (%s,%s,%s)", (temp_dict['id_employer'],
                                                                    temp_dict['employer_name'],
                                                                    temp_dict['industries']))
            cur.execute("SELECT * FROM employers")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        self.conn.commit()


    def insert_vacancies(self, vacancies_list):
        """Записывает информацию о компании в БД"""
        with self.conn.cursor() as cur:
            for row in vacancies_list:
                cur.execute("INSERT INTO vacancies VALUES (%s,%s,%s,%s,%s,%s)", (row['title'],
                                                                           row['salary_from'],
                                                                           row['salary_to'],
                                                                           row['requirement'],
                                                                           row['link'],
                                                                           row['employer_name']))
            cur.execute("SELECT * FROM vacancies")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """Выводит количество вакансий у компаний"""
        with self.conn.cursor() as cur:
            cur.execute("""SELECT employers.employer_name, COUNT(vacancies.title) FROM employers LEFT JOIN vacancies 
            ON employers.employer_name = vacancies.employer_name GROUP BY employers.employer_name""")
            result = cur.fetchall()
        return result

    def get_all_vacancies(self):
        """ Вывод вакансий компании с зп и ссылкой"""
        with self.conn.cursor() as cur:
            cur.execute("""SELECT employer_name,title, salary_from, salary_to,url 
             FROM vacancies """)
        result = cur.fetchall()

        return result

    def get_avg_salary(self):
        """Выводит среднюю зарплату"""
        with self.conn.cursor() as cur:
            cur.execute("""SELECT (AVG(salary_from)+AVG(salary_to))/2 AS average  FROM vacancies """)
            result = cur.fetchone()
        return result

    def get_vacancies_with_higher_salary(
            self):  # поиск вакансии по средней зп и фильтрации выше нее
        self.cur.execute(
            """SELECT AVG(CAST(salary AS numeric)) FROM vacancies""")
        avg_salary = self.cur.fetchone()[0]
        self.cur.execute(
            f"""SELECT * FROM vacancies WHERE CAST(salary AS numeric) > {avg_salary}""")
        result = self.cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, word):
        self.cur.execute(
            f"SELECT * FROM vacancies WHERE title LIKE '%{word}%'")
        result = self.cur.fetchall()
        return result

    def close_conn(self):
        """Закрывает сonn"""
        self.conn.close()