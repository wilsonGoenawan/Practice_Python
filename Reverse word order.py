import utils as ut

words = ut.get_string("input more than one word sentences: ")
def Reverse(lists):
    temp = []
    for i in range(len(lists)-1,0,-1):
        temp.append(lists[i])
    return temp
def split(words):
    return words.split()
def join(words):
   return ' '.join(words)

print(join(Reverse(split(words))))
