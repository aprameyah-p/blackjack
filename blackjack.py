
## Diamonds, Hearts, Clubs, Spades
##. D(1-13), H(14-26), C(27-39), S(40-52)'''


import time
import random

suits=["D","H","C","S"]
ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def card_deck():
    all_card_list=[]
    for suit in suits:
        for rank in ranks:
            all_card_list.append([suit,rank])
    random.shuffle(all_card_list)
    return all_card_list

def draw_card(deck):
    return deck.pop()

def card_drawing(card):
    top_left=chr(9484)
    horizontal_line=chr(9472)
    top_right=chr(9488)
    bottom_left=chr(9492)
    bottom_right=chr(9496)
    vertical_line=chr(9474)
    if card[0]=="D":
        suit_symbol=chr(0x2666)
    elif card[0]=="H":
        suit_symbol=chr(0x2665)
    elif card[0]=="C":
        suit_symbol=chr(0x2663)
    else:
        suit_symbol=chr(0x2660)
    print(top_left,horizontal_line,horizontal_line, horizontal_line, top_right,sep="")
    print(vertical_line,suit_symbol.center(3),vertical_line,sep="")
    print(vertical_line,card[1].center(3),vertical_line,sep="")
    print(bottom_left,horizontal_line,horizontal_line, horizontal_line,bottom_right,sep="")


def CardValue(CardList):
    card_value=0
    a_count=0
    for Card in CardList:
        if Card[1] in "23456789" or Card[1]=="10":
            card_value+=int(Card[1])
        elif Card[1] == "A":
            a_count+=1
            card_value+=1
        else:
            card_value+=10
    if a_count and card_value+10<=21:
        card_value+=10

    return card_value


def BlackJack():
    ''' 1) deal the dealer cards
        2) deal the player cards
        3) ask the player if they wanna twist/stick
        4) ez
    '''
    player_bust=False
    dealer_bust=False
    player_blackjack=False
    dealer_blackjack=False
    deck=card_deck()

    DealerCards=[draw_card(deck),draw_card(deck)]
    print("Dealers Cards are:")
    card_drawing(DealerCards[0])
    time.sleep(1.5)
    PlayerCards=[draw_card(deck),draw_card(deck)]
    print("Your Cards are:")
    card_drawing(PlayerCards[0])
    time.sleep(1.5)
    card_drawing(PlayerCards[1])
    print("The Value of your cards is:", CardValue(PlayerCards))


    # check for blackjack
    if CardValue(PlayerCards)==21:
        player_blackjack=True
    if CardValue(DealerCards)==21:
        dealer_blackjack=True

    if player_blackjack or dealer_blackjack:
        print("Dealer's Second Card is:")
        card_drawing(DealerCards[1])
        time.sleep(1)

    if player_blackjack and dealer_blackjack:
        print("Both have Blackjacks! Tie!")
        return
    elif player_blackjack:
        print("Blackjack! You Win!")
        return
    elif dealer_blackjack:
        print("Dealer gets Blackjack! Dealer Wins!")
        return

    while True:
        print("Do you want to Twist or Stick (T/S): ",end="")
        while True:  
            twist_stick_choice=input()
            if twist_stick_choice.upper() in ("T","S"):
                break
        if twist_stick_choice.upper() == "T":
            PlayerCards.append(draw_card(deck))
            card_drawing(PlayerCards[-1])
            if CardValue(PlayerCards)>21:
                print("Bust!")
                player_bust=True
                break
            elif CardValue(PlayerCards)==21:
                print("You hit 21!")
                break
            else:
                print("The Value of your cards is:", CardValue(PlayerCards))
        else:
            
            break



    print("Dealer's Second Card is:")
    card_drawing(DealerCards[1])
    time.sleep(1)


    if CardValue(DealerCards)<17 and player_bust==False:
        print("The Dealer Draws:")
    while CardValue(DealerCards)<17 and player_bust==False:
        DealerCards.append(draw_card(deck))
        card_drawing(DealerCards[-1])
        if CardValue(DealerCards)>21:
            print("Dealer Bust!")
            dealer_bust=True
            break

    print("The Value of the dealers cards is:", CardValue(DealerCards))
    print("The Value of your cards is:", CardValue(PlayerCards))


    if player_bust:
        print("Dealer Wins!")
    elif dealer_bust:
        print("Player Wins!")
    elif CardValue(DealerCards)>CardValue(PlayerCards):
        print("Dealer Wins!")
    elif CardValue(DealerCards)==CardValue(PlayerCards):
        print("Tie!")
    else:
        print("Player Wins!")


def menu():
    while True:
        print("1. Play Blackjack")
        print("2. Exit")
        menu_input=input("enter your choice:")
        if menu_input=="1":
            BlackJack()
        elif menu_input=="2":
            return


if __name__ == "__main__":
    menu()







