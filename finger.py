#date 05-08-24
#write a program that examines 3 variables and print the larges odd number among them, if none of them are odd it should print a message to that.


def odd_number(a,b,c):
    #define list of numbers
    my_numbers = [a,b,c]
    new_list = []

    #loop for cheking the list and output if is even or odd
    for item in my_numbers:
        #if theres only even numbers
        if item % 2 == 0:
            a = 'There is no odd number'
        #getting the odd numbers
        else:
            new_list.append(item)
    #if you want to show the list of odd numbers
    #print(new_list)
    
    #count the itens of the list
    index_range = len(new_list)
    
    #if lists has less than 3 odd numbers and can't be empty
    if index_range <= 2 and index_range != 0:
        if new_list[0] > new_list[1]: 
            print (new_list[0],'its the largest odd number')          
        else:
            print (new_list[1], 'its the largest odd number')
    #if list has 3 odd numbers
    if index_range > 2:
        if new_list[0] > new_list[1] or new_list[0] > new_list[2]:
            print (new_list[0],'its the largest odd number')        
        elif new_list[1] > new_list[2]:
            print (new_list[1],'its the largest odd number')
        else:
            print (new_list[2],'its the largest odd number')

    if index_range == 0:
        print(a)

#test1
#odd_number(6,8,10)

#test2
#odd_number(3,5,9)

