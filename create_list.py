'''Use List Comprehension to create
 a list of the first letters of every word in the string below:'''

st = 'Create a list of the first letters of every word in this string'

lista = st.split(' ')

for letra in lista:
    print(letra[0])
