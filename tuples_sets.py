# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create a tupple
#fruits =('Apples', 'Oranges', 'Grapes')
#print(type(fruits))

#single value needs a trailing coma
#fruits2 = ('Apples', )

#get a value
#print(fruits[1])

#cant change
#fruits[0] = 'Peers'

#delete a tuple
#del fruits2

#length
#print(len(fruits))
# A Set is a collection which is unordered and unindexed. No duplicate members.

#create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#check if something is in set
#print('Apples' in fruits_set)

#add to set
fruits_set.add('Banana')
print(fruits_set)

#remove from set
fruits_set.remove('Banana')
print(fruits_set)

#add twice
fruits_set.add('Mango')
print(fruits_set)
#clear set
#fruits_set.clear()
#print(fruits_set)

#delete set
#del fruits_set
#print(fruits_set)