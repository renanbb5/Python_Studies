# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#sample json
userJSON = '{"first_name": "Renan", "last_name": "Borges", "age": 30}'

#parses_dictionary
user = json.loads(userJSON)


print(user)
print(user['first_name'])

car = {'make': 'Honda', 'year': '2014'}
carJSON = json.dumps(car)
print(carJSON)
