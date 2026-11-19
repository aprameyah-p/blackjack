'''for i in range (0x2500,0x256f):
    print(chr(i), end=" ")
print()

print(chr(0x2660))
print(chr(0x1f0a1))

## Diamonds, Hearts, Clubs, Spades
##. D(1-13), H(14-26), C(27-39), S(40-52)'''


import time
import math
import random

AlreadyPulled=[]

suits=["D","H","C","S"]
ranks=['A','2','3','4','5','6','7','8','9','10','K','Q','J']
card_list=[]

def CardShuffle():

    for suit in suits:
        for rank in ranks:
            card_list.append([suit,rank])

    random.shuffle(card_list)
    new_card=card_list.pop()
    return new_card


def CardValue(CardList):
    card_value=0
    a_flag=False
    a_is_one_flag=False
    for Card in CardList:
        if Card[1] in "23456789" or Card[1]=="10":
            card_value+=int(Card[1])
        elif Card[1] == "A":
            a_flag=True
            if card_value>21:
                card_value+=1
                a_is_one_flag=True
            else:
                card_value+=11
                a_is_one_flag=False
        else:
            card_value+=10
    if card_value>21:
        if a_flag:
            if not a_is_one_flag:
                card_value-=10
    return card_value


def BlackJack():
    ''' 1) deal the dealer cards
        2) deal the player cards
        3) ask the player if they wanna twist/stick
        4) ez
    '''

    DealerCards=[CardShuffle(),CardShuffle()]
    print("Dealers Cards are:")
    print(DealerCards[0])
    time.sleep(1.5)
    print(DealerCards[1])
    time.sleep(1)
    PlayerCards=[CardShuffle(),CardShuffle()]
    print("Your Cards are:")
    print(PlayerCards[0])
    time.sleep(1.5)
    print(PlayerCards[1])

    while True:
        print("Do you want to Twist or Stick (T/S): ",end="")
        while True:  
            twist_stick_choice=input()
            if twist_stick_choice.upper() in ("T","S"):
                break
        # Case 1: Twist, draw 1 more card, may bust, may win, make function
        if twist_stick_choice.upper() == "T":
            PlayerCards.append(CardShuffle())
            print(PlayerCards[-1])
            print("The Value of your cards is:", CardValue(PlayerCards))
            if CardValue(PlayerCards)>21:
                print("Bust!")
                break
        else:
            break

    print("The Value of the dealers cards is:", CardValue(DealerCards))
    print("The Value of your cards is:", CardValue(PlayerCards))

    while True:
        if CardValue(DealerCards)>CardValue(PlayerCards):
            print("Dealer Wins!")
            break
        elif CardValue(DealerCards)==CardValue(PlayerCards) and CardValue(DealerCards)>17:
            print("Tie!")
            break
        elif CardValue(DealerCards)==CardValue(PlayerCards) and CardValue(DealerCards)<17:
            DealerCards.append(CardShuffle())
        else:
            print("Player Wins!")


if __name__ == "__main__":
    BlackJack()







