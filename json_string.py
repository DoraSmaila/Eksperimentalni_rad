import timeit

setup_code = """
import requests

base_url = 'http://localhost:8000/'
"""

read_profesori_code = """
response = requests.get(base_url + 'read_profesori/')
profesori_json = response.json()
"""

read_predmeti_code = """
response = requests.get(base_url + 'read_predmeti/')
predmeti_json = response.json()
"""

profesori_time = timeit.timeit(stmt=read_profesori_code, setup=setup_code, number=100)
predmeti_time = timeit.timeit(stmt=read_predmeti_code, setup=setup_code, number=100)

print(f'Vreme čitanja Profesora: {profesori_time} sekundi')
print(f'Vreme čitanja Predmeta: {predmeti_time} sekundi')
