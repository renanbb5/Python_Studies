def myfunc( a, b ,c):
    d = a + b + c
    for i in range (1,12):

        if d <= 21:

            return d
        
        elif d > 21 and a == 11 or b == 11 or c ==11:

            return d - 10
        
        else:
            return "BURST"

print(myfunc(9,9,11))
        
