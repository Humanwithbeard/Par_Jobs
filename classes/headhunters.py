import json
import requests
from classes.abstractclass import GetVacancies


class HeadHunter(GetVacancies):
    """
    Класс получения вакансий с сайта hh.ru
    """
    def __init__(self, search_query, salary=None, show_salary=False):
        self.search_query = search_query
        self.salary = salary
        self.show_salary = show_salary

    def get_vacancies(self):
        params = {
            'text': self.search_query,
            'area': 113,
            'per_page': 100,
            'salary': self.salary,
            'only_with_salary': self.show_salary,
            'currency': 'RUR'
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        hh_json = json.loads(data)
        return hh_json
