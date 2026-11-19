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

CardDict={}
AlreadyPulled=[]

def CardShuffle():
    while True:
        CardNumber=int(random.randint(1,52))
        if CardNumber in AlreadyPulled:
            pass
        else:
            break
    AlreadyPulled.append(CardNumber)
    if CardNumber <= 13 and CardNumber >= 1:
        CardSuit="D"
    elif CardNumber <= 26 and CardNumber >= 14:
        CardSuit="H"
    elif CardNumber <= 39 and CardNumber >= 27:
        CardSuit="C"
    else:
        CardSuit="S"


    if CardSuit == "D":
        if CardNumber<=10:
            CardValue=CardNumber
        else:
            CardValue=10
    elif CardSuit == "H":
        if CardNumber<=23:
            CardValue=CardNumber-13
        else:
            CardValue=10
    elif CardSuit == "C":
        if CardNumber<=36:
            CardValue=CardNumber-26
        else:
            CardValue=10
    elif CardSuit == "S":
        if CardNumber<=49:
            CardValue=CardNumber-39
        else:
            CardValue=10
    return [CardSuit,CardValue]

def BlackJack():
    ''' 1) deal the dealer cards
        2) deal the player cards
        3) ask the player if they wanna twist/stick
        4) ez
    '''
    PlayerScore=0
    DealerScore=0


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


    for PCard in PlayerCards:
        PlayerScore+=PCard[1]

    for DCard in DealerCards:
        DealerScore+=DCard[1]


    while True:
        print("Do you want to Twist or Stick (T/S): ",end="")
        while True:  
            TwistStickChoice=input()
            if TwistStickChoice.upper() in "TS":
                break
        if TwistStickChoice in "Tt":
            if PlayerScore>17:
                print("Can't Twist when over 17")
                pass
            PlayerCards.append(CardShuffle())
            LastCard=PlayerCards[-1]
            PlayerScore+=LastCard[1]
            print(LastCard)
            if PlayerScore>21:
                print("Bust! Dealer Wins!")
                break
            elif PlayerScore==21:
                print("Blackjack! You Win!")
                break
            else:
                print("Your Score is:", PlayerScore)

        else:
            if PlayerScore>DealerScore and DealerScore<=17:
                DealerCards.append(CardShuffle())
                LastCard=DealerCards[-1]
                DealerScore+=LastCard[1]
            elif PlayerScore==DealerScore and DealerScore<=17:
                DealerCards.append(CardShuffle())
                LastCard=DealerCards[-1]
                DealerScore+=LastCard[1]
            else:
                pass
            if DealerScore>21:
                print("Dealer Busted! You Win!")
            elif DealerScore==21:
                print("Dealer hit Blackjack! you Lose!")
            elif PlayerScore>DealerScore:
                print("You WIN!")
            else:
                print("You Lose!")
            break

BlackJack()
















