import random

#make 2 random list of length below 10
list_a = random.sample(range(100),random.randint(4,10))
list_b = random.sample(range(100),random.randint(3,10))
print(list_a)
print(list_b)

common_element = list(set(x for x in list_a if x in list_b))
print(common_element)

