# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Renan'
age = 31

print(f"My name is {name} and I'm {age} years old!")

# String Formatting

# String Methods

#capitalize
s = 'helloworld'
print(s.capitalize())

#upper
print(s.upper())

#lower
print(s.lower())

#swapcase
print(s.swapcase())

#get lenght
print(len(s))

#replace
print(s.replace('hello', 'renan'))

#count
sub = 'r'
print(s.count('r'))

#starts with
print(s.startswith('hello'))

#ends with
print(s.endswith('d'))

#split into a list
print(s.split())

#find position
print(s.find(''))

#is all alphanumeric
print(s.isalnum())
#its all alphabetic
print(s.isalpha())
#its all numeric
print(s.isnumeric())