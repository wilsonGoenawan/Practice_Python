import utils as ut


number= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]



while True:
    filtered_num = []
    cutoffpoint = ut.get_number("cut off point = ")
    if cutoffpoint == -1:
        break
    for num in number:
        if num <=cutoffpoint:
            filtered_num.append(num)
        
    print("list of number below 5 = ", filtered_num )

