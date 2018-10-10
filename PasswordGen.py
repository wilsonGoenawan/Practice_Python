import random 
import utils as ut


Capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
special ="!@#$%^&()"
def capital(length):
    new = []
    while len(new)!= length:
        new.append(random.choice(Capital))
    return new

def low(length):
    new = []
    while len(new)!= length:
        new.append(random.choice(lower))
    return new

def numbers(length):
    new = []
    while len(new)!= length:
        new.append(random.choice(number))
    return new

def specials(length):
    new = []
    while len(new)!= length:
        new.append(random.choice(special))
    return new

def rand(length):
    new = []
    while len(new)!= length:
        new.append(random.choice(special+Capital+lower+number))
    return new



def Strong_pass(length):
    new = []
    new = capital(1)+ low(1)+ numbers(1)+ specials(1)+ rand(length-4)
    return new 
    

paslen = ut.get_number("length of your password: ")
strength = ut.get_number("1.Strong /nenter your password strength: ")

if strength == 1:
    print(Strong_pass(paslen))

