from class_API import  HН_employer

from pprint import pprint

from class_DBManager import DBManager

employers_id=[1552384, 3529, 15478, 6093775, 67611, 80, 1740, 2381, 2987, 115]

#Url = "https://api.hh.ru/vacancies?employer_id=1455"
#Url = "https://api.github.com"
def main():
    for id_employer in employers_id:
        employer = HН_employer(id_employer)
        DBM = DBManager()
        #employer.get_vacancy(1)
        #DBM.insert_employer(employer.format_employer())
        #DBM.insert_vacancies(employer.format_vacancies())


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
            for line in DBM.get_companies_and_vacancies_count():1
                print(line)
            # Обработка команды 2: ТОП вакансий
        elif command == '2':
            print('2')
        # Обработка команды 3: Вывод на экран вакансий зарплаты в которых попадают в указанный дипазон
        elif command == '3':
            print('3')
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
