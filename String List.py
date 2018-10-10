import utils as ut


string = ut.get_string("input string: ")
check = 0
length = len(string)
for i in range(0,length-1):
    if string[i] == string[length-i-1]:
        check += 1
    else:
        print(i)
        break
if check == length-1:
    print("This is a palindrome.")
    print(check)
else:
    print("This is not a palindrome.")
    print(check)
