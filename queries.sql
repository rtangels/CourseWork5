CREATE TABLE employers
(
id_employer int PRIMARY KEY,
employer_name varchar(100) UNIQUE,
industries varchar(250)
);

CREATE TABLE vacanciaes
(
title varchar(100),
salary_from int,
salary_to int,
requirement text,
employer_name varchar REFERENCES employers(employer_name) NOT NULL
);
