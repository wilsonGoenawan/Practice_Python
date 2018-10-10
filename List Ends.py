import utils as ut
import random

a = random.sample(range(100),random.randint(1,10))# make a random list

def first_last(lists):
    result = [lists[0],lists[-1]]
    return result
print(first_last(a))
print(a)
