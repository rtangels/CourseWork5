# import urllib library
from urllib.request import urlopen

import json

import requests

class ParsingError(Exception):
    """Пользовательский класс ошикок"""

    def __str__(self):
        """Возвращает текст ошибки"""
        return 'Ошибка получения данных'

class HН_employer():
    def __init__(self, employer_id):
        """конструктора класса для API hh.ru"""
        self.__header = {
            'User-Agent': 'Mozilla/5.0 (platform; rv:gekoversion)  Gecko/geckotrail YaBrowser/23.3.3.719'}
        self.__params ={
            "page": 0,
            "per_page": 100
        }
        self.__name = ''
        self.__vacancies = []
        self.__employer_id = employer_id


    def get_request(self):
        """Получение ответа на запрос по компании"""
        path='https://api.hh.ru/employers/'+str(self.__employer_id)

        response = requests.get(path,
                                headers=self.__header
                                )
        if response.status_code != 200:
            raise ParsingError
        return response.json()

    def vacancy_get_request(self):
        """Получает ответ на запрос вакансий компании"""
        try:
            data = self.get_request()
        except  ParsingError:
            print('Ошибка получения данных!')

        vacancies_url = data['vacancies_url']
        # получает ответ на запрос  url
        response = requests.get(vacancies_url, params=self.__params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['items']




    def get_vacancy(self, page_count=1):
        """Формирует список вакансий"""

        while self.__params['page'] < page_count:
            print(
                f"Cбор сведений hh, страница{self.__params['page'] + 1}",
                end=": ")
            try:
                values = self.vacancy_get_request()
            except  ParsingError:
                print('Ошибка получения данных!')
                break
            print(f"Найдено ({len(values)}) вакансий \n")
            self.__vacancies.extend(values)
            self.__params['page'] += 1

    def see_vacancy(self):
        """Выдаёт информацию по вакансиям"""
        information = self.__vacancies
        return information

    @staticmethod
    def get_salary(salary):
        """Приводит зарпалату к зарплате в одной валюте"""
        formated_salary = [None, None]
        if salary and salary['from'] and salary['from'] != 0:
            if salary['currency'].lower() == 'rur':
                formated_salary[0] = salary['from']
            elif salary['currency'].lower() == 'eur':
                formated_salary[0] = salary['from'] * 84
            else:
                formated_salary[0] = salary['from'] * 78

        if salary and salary['to'] and salary['to'] != 0:
            if salary['currency'].lower() == 'rur':
                formated_salary[1] = salary['to']
            elif salary['currency'].lower() == 'eur':
                formated_salary[1] = salary['to'] * 84
            else:
                formated_salary[1] = salary['to'] * 78
        return formated_salary

    def format_vacancies(self):
        """Возвращает вакансии в формате удобном для заполнения БД"""
        vacancies = []
        if self.__vacancies:
            for row in self.__vacancies:
                salary_from, salary_to = self.get_salary(row['salary'])
                temp_dict = {
                    'title': row['name'],
                    'salary_from': salary_from if salary_from else 0,
                    'salary_to': salary_to if salary_to else 0,
                    'requirement': row['snippet']['requirement'],
                    'link': row['alternate_url'],
                    'employer_name': row['employer']['name']
                }
                vacancies.append(temp_dict)
        return vacancies

    def format_employer(self):
        """Возвращает данные о компании для заполнения БД"""
        data = self.get_request()
        temp_dict = {
            'id_employer': int(self.__employer_id),
            'employer_name': data['name'],
            'industries': data['industries'][0]['name']

        }
        return temp_dict





