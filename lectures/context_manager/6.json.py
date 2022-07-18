import json

person_data = {
    'name': 'Oleksii',
    'money': 29.1
}
print(person_data)

a = json.dumps(person_data)
print(a, type(a))  # in json-file all data have to be only in double quotes ", not in single ones - '
print(json.loads(a)['name'])


