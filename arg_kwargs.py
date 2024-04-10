def myfunc(input_string):
    result = ""
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result
myfunc('teste')