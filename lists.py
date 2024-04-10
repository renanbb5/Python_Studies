# A List is a collection which is ordered and changeable. Allows duplicate members.

#create list

numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'peach', 'pinnaple']
#use a constructor
#numbers2 = list((1, 2, 3, 4, 5))

#get a value
print(fruits[0])

#get length
print(len(fruits))

#append
fruits.append('mango')
print(fruits)

#remove
fruits.remove('pinnaple')
print(len(fruits))

#insert into position 
fruits.insert(0, 'grapes')
print(fruits)

#change value
fruits[0] = 'guarana'
#remove with pop

fruits.pop(2)
print(fruits)

#reverse list
fruits.reverse()
print(fruits)

#sort list
fruits.sort()
print(fruits)

