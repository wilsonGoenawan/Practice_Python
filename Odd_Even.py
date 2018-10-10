def get_number(inputText='input: ', *args):
    number = int(input(inputText))
    return number
 
num1 = 0
while True:
    num1 = get_number()
    num2 = get_number()
    if num1 == -1:
        print("bye-bye")
        break
    elif num1 % num2 == 0:
        print("%i is multiple of %i" %(num1,num2))
    else:
        print("%i is not multiple of %i" %(num1,num2))
