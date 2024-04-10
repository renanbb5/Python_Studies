def square(num):
    return num ** 2

my_num = [1, 2, 3, 4, 5]

for item in map(square, my_num):
    print(item)

print(list(map(square, my_num)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    
names = ['Andy', 'Sally', 'Chica']

print(list(map(splicer, names)))

def check_even(num):
    return num % 2 == 0

my_num2 = [1, 2, 3, 4, 5, 6]

for n in filter(check_even,my_num2):
    print(n)

a = list(map(lambda num: num ** 2, my_num2))
print(a)

b = list(filter(lambda num:num % 2 == 0 ,my_num2))
print(b)

c = list(map(lambda name: name[::-1],names ))
print(c)