from class_API import  HН_employer

from pprint import pprint

from class_DBManager import DBManager

employers_id=[1552384, 3529, 15478, 6093775, 67611, 80, 1740, 2381, 2987, 115]


def main():
    for id_employer in employers_id:
        employer = HН_employer(id_employer)
        DBM = DBManager()
        employer.get_vacancy(3)
        DBM.insert_employer(employer.format_employer())
        DBM.insert_vacancies(employer.format_vacancies())


    while True:
        command = input(f"""\nВведите обозначение команды:
    1: Вывести список всех компаний и количество вакансий в них
    2: Вывести список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
    3: Вывсти среднюю зарплату по вакансиям.
    4: Вывести список всех вакансий, у которых зарплата выше средней по всем вакансиям.
    5: Вывести список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
    exit: Выйти из программы\n""")
        # Обработка команды 1:Сортировка вакансий
        if command == '1':
            for line in DBM.get_companies_and_vacancies_count():
                print(line)
            # Обработка команды 2 :все вакансии
        elif command == '2':
            for row in DBM.get_all_vacancies():
                print(row)
        # Обработка команды 3: Вывод на экран средней зарплаты
        elif command == '3':
            print(DBM.get_avg_salary())
        # Обработка команды 4: Вывод вакансий с большей зарплатой,чем средняя
        elif command == '4':
            for row in DBM.get_vacancies_with_higher_salary():
                print(row)
        elif command == '5':
            word = input('Введите слово\n')
            if DBM.get_vacancies_with_keyword(word):
                for row in DBM.get_vacancies_with_keyword(word):
                   print(row)
            else:
                print('Нет вакансий с таким словом')
        elif command.lower() == 'exit':
            DBM.close_conn()
            break
        else:
            print('Неверная команда')
    DBM.close_conn()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()


#
