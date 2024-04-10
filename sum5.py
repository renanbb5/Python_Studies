total = 0
for i in range(0,1000):
    
    if i % 5 == 0 or i % 3 == 0 :
        print(i)
        total += i
    else:
        pass
print('Soma dos múltiplos de 3 e 5:',total)