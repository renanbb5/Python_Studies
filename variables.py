# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

'''
x = 1           # int
y = 1.5         #float
name = 'joão'   #str
is_cool = True  #bool

'''
#this is a multiple assignment

x,y,name,is_cool = (1,1.5,'joão',True)


#basic math 
a = x + y

#casting
a = str(name)
y = int(y)
z = float(y)
print(type(z), z)

