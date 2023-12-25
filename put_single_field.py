import timeit
import requests

setup_code = """
import requests

base_url = 'http://localhost:8000/'
profesor_id = 1  # Zamijenite sa stvarnim ID-jem profesora kojeg želite ažurirati
new_value = 'Novo Ime'  # Zamijenite sa stvarnom novom vrijednošću polja koje želite ažurirati
"""

update_single_field_code = """
response = requests.put(f'{base_url}update_single_field/{profesor_id}/', json={'new_value': new_value})
"""

time_to_update = timeit.timeit(stmt=update_single_field_code, setup=setup_code, number=1)

print(f'Vrijeme odgovora na putanju za ažuriranje jednog polja: {time_to_update} sekundi')
