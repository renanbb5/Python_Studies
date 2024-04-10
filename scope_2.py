x = 50 

def func():
    global x
    print(f' X is {x}')

    #LOCAL ASSIGNMENT IN a global

    x = 'new value'

    print(f'I JUST LOCALLY CHANGED global X TO {x}')

print(func())

print(x)