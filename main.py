from class_API import  HН_employer

from pprint import pprint

from class_DBManager import DBManager

#Url = "https://api.hh.ru/vacancies?employer_id=1455"
#Url = "https://api.github.com"
def main():
    employer = HН_employer(1552384)
    DBM = DBManager()
    #employer.get_vacancy(1)
    #print(len(employer.see_vacancy()))
    #pprint(employer.format_vacancies()[0])
    DBM.insert_employer(employer.format_employer())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()


#
