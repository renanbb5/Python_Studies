#return all the even numbers in a list
def check_even_list(num_list):
#first we define a place holder
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
    
        else:
            pass

    return even_numbers

print(check_even_list([2]))