lista = [3,1,3]

def find_33(lista):
    
    if lista[0] == lista[1]:
        
        return f'Valor {lista[0]} é igual a {lista[1]}'
    
    elif lista[1] == lista[2]:
        
        return f'Valor {lista[1]} é igual a {lista[2]}'
    
    else:
        return f'Não tem valores iguais um ao lado do outro'

print(find_33(lista))
    