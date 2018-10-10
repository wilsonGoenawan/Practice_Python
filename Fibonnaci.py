import utils as ut

def fibonaci(length,new):
    while len(new) != length:
        if len(new)== 0:
            new.append(1)
        elif len(new)== 1:
            new.append(1)
        elif len(new)!= length:
            new.append(new[-1]+new[-2])
    return new


a = []
while True:
    length = ut.get_number("input length of fibonaci number: ")
    if length < 1:
        break
    print(fibonaci(length,a))
    print("input negative to exit")
