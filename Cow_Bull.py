import random 
import utils as ut 

count = 0
num = random.sample(range(10),4)

def bull(num,array_number):
    num = str(num)
    bull = list(set([common for common in num if common in array_number ]))
    return len(bull)

def cow(random_num, array_number):
    cow = 0
    for i in range(0,4):
        if str(random_num[i]) == array_number[i]:
            cow += 1
    return cow

answer = num
while True:
   
    in_num = ut.get_string("input your number here: ")
    if int(in_num) < 0:
        print("answer is {}".format(num))
        break
    print("cow = {}".format(cow(num,in_num)))
    print("Bull = {}".format(bull(num,in_num)))
    


    count += 1
    if cow(num,in_num) == 4 : 
        print("Thank you for playing. \nYou got it in {} tries".format(count))
        print("The answer is {}".format(in_num))

        break

