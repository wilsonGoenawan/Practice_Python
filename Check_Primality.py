import utils as ut

while True:
    number = ut.get_number("input your number: ")
    divisor = ut. divisor(number)
    if len(divisor) == 2:
        print("{} is a prime number".format(number))
    else:
        print("{} is not a prime number".format(number))
    
    cont = ut.get_string("press n to exit\n")
    if cont == "n":
        break
    else:
        print("continueing...")
    
