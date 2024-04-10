def almost_there(n):

        valor1 = 100 - abs(n)
        
        valor2 = 200 - abs(n) 

        if abs(valor1) > 0 and abs(valor1) <= 10:
            
            return valor1, f'Less than 10. You need  {valor1} steps'    
        
        elif abs(valor2) > 0 and abs(valor2) <=10:
            
            return valor2, f'Lee than 10. You need {valor2} steps'
        else:
            return False, "Higher than 10", "From 100",valor1, "From 200", valor2

print(almost_there(150))
