#создание таблицы компаний
CREATE TABLE employers
(
id_employer int PRIMARY KEY,
employer_name varchar(100) UNIQUE,
industries varchar(250)
);

# создание таблицы компаний
CREATE TABLE vacancies
(
title varchar(100),
salary_from int,
salary_to int,
requirement text,
url varchar(150),
employer_name varchar REFERENCES employers(employer_name) NOT NULL
);

#вывод компаний и количество их вакансий
SELECT employers.employer_name, COUNT(vacancies.title) FROM employers LEFT JOIN vacancies
            ON employers.employer_name = vacancies.employer_name GROUP BY employers.employer_name
#вывод вакансий в виде : компания, наименование вакансии , зарплата, ссылка
SELECT employer_name,title, salary_from, salary_to,url FROM vacancies

#вывод средней зарплаты
SELECT CAST((AVG(salary_from)+AVG(salary_to))/2 AS int)  FROM vacancies

#вывод всех вакансии с зарплатой больше средней
SELECT title, salary_from, salary_to FROM vacancies
WHERE CAST(salary_from AS numeric) > {avg_salary}
OR CAST(salary_from AS numeric) > {avg_salary}

#вывод вакансий в названии которых есть определённое слово (word)
SELECT * FROM vacancies WHERE title LIKE '%{word.title()}%'
OR title LIKE'%{word.lower()}%' OR title LIKE '%{word.upper()}%'

#

