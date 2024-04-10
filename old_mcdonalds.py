def old_mcdonald(name):
    
    lista = str(name.split())
    
    return lista[0:5].title() + lista[5:13].capitalize()

print(old_mcdonald('macdonald'))