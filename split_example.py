#exercise
'''Use for, .split(), and if to create a Statem
ent that will print out words that start with 's':'''

st = 'Print only the words that start with s in this sentence'

for word in st.split(' '):
    if word[0] == 's' :
        print(word)
    