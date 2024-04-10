#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

nova_lista = st.split()
letra = 0
for i in nova_lista:
    letra += 1
    if letra % 2 == 0:
        print('')
    else:
        print(letra,i)
        
