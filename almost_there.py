def almost_there(n):

        valor1 = 100 - abs(n)
        
        valor2 = 200 - abs(n) 

        if abs(valor1) > 0 and abs(valor1) <= 10:
            
            return valor1, f'Menor que Dez. Faltam {valor1} casas'    
        
        elif abs(valor2) > 0 and abs(valor2) <=10:
            
            return valor2, f'Menor que dez faltam {valor2} casas'
        else:
            return False, "Maior que 10 casas", "Em relação ao 100",valor1, "Em relação a 200", valor2

print(almost_there(150))