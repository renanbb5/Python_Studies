# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create a dictionary
person = {
    'first_name': 'Renan',
    'last_name': 'Borges',
    'age' : 31
}

#create a dictionary using constructor
person2 = dict(first_name='Sara', last_name='Willians')

#print(person, type(person))
#print(person2, type(person2))

#get value
#print(person['first_name'])
#print(person2['last_name'])
#print(person.get('last_name'))

#add a key value 
person2['phone'] = '555-555-555'
#print(person2)

#get dict keys
#print(person.keys())

#get dict items
#print(person.items())

#list of dictionaries
people = [
    {'name': 'Martha', 'age' :30},
    {'name': 'Renan', 'age' : 31 }

]
print(people[0]['name'])