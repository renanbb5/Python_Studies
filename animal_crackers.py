
def myfunc(palavra):
    lista = palavra.split(', ')
   
   
    for palavra in lista:
   
        if palavra[0] == palavra[12]:
            
            return True
        
        else:
            
            return False
    

print(myfunc('Levelheaded Llama'))
print(myfunc('Crazy Kangaroo'))


    