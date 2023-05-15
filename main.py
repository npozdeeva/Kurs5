from DBManager import DBManager
from HH_class import HH


def main():
    db = DBManager()
    hh = HH()
    vacancies = hh.get_vacancies()
    db.save_vacancies(vacancies)
    companies_vacancies_count = db.get_companies_and_vacancies_count()
    print("Количество вакансий компании:")
    for row in companies_vacancies_count:
        print(row[0], "-", row[1])

    all_vacancies = db.get_all_vacancies()
    print("Список всех вакансий:")
    for row in all_vacancies:
        print(row)

    avg_salary = db.get_avg_salary()
    print("Средняя з\п:", avg_salary)

    high_salary_vacancies = db.get_vacancies_with_higher_salary()
    print("Список вакансий с зарплатой выше средней:")
    for row in high_salary_vacancies:
        print(row[0])

    keyword = "Python"
    vacancies_with_keyword = db.get_vacancies_with_keyword(keyword)
    print(f"Список вакансий, использующих '{keyword}':")
    for row in vacancies_with_keyword:
        print(row[0], "-", row[1], "-", row[2])


if __name__ == '__main__':
    main()