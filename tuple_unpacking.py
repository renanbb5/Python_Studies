
work_hours = [('Abby',500),('Josh',7700),('Andrew',1000)]
def empoyee_check(work_hours):

    current_max = 0
    employee_month = ['']

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_month = employee
        else:
            pass
    #Return
    return(employee_month,current_max)

print (empoyee_check(work_hours))
item = empoyee_check(work_hours)
print(item)