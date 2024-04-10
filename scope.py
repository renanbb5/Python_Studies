#GOLBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    #ENCLOSING
    name = 'Renan'

    def hello():
        #LOCAL
        name = 'I M A LOCAL'
        print('Hello ' + name)
    
    print(hello())

print(greet())