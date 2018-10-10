def get_number(inputText='input: ', *args):
    number = int(input(inputText))
    return number

def get_string(inputText='input: ', *args):
    string = input(inputText)
    return string

def divisor(number):
    divisor =[]
    for check in range (1,number+1):
        if number % check == 0:
            divisor.append(check)
    return divisor
