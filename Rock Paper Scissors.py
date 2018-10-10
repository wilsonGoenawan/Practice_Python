import utils as ut
import random

def check_win(self,opp):
    if self == opp:
        print("draw")
    elif self == 3 and opp == 1:
        print("You win!!")

    elif opp == (self + 1) :
        print("You win!!")
    
    else:
        print("Opponent win!")



play_again = True
while play_again is True:
    print("please pick your play: \n1.rock \n2.scissor \n3.paper \n4.exit")
    pick = ut.get_number("input the number: ")
    opp_pick = random.randrange(1,4)
    if pick == 4:
        break
    print(opp_pick)
    check_win(pick,opp_pick)
    
    
