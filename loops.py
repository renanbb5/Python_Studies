# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Renan', 'Melissa', 'Kitty']

#simple lood
#for person in people:
#    print(f'Current person: {person}')


#break
#for person in people:
#    if person == 'Melissa':
#        break
#    print(f'Current person: {person}')

#continue
#for person in people:
#    if person == 'Renan':
#        continue
#    print(f'Current person: {person}')

#for i in range(len(people)):
#    print(people[i])

#for i in range(0, 999999999999999999999999999):
#    print(f'Number: {i}')
    
# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
