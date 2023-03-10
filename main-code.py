import time
import random

# Game Cards

card_pack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
opponent_names = ["kingping", "hannah", "taylor", "benedict", "cambio", "tigersugar", "jasmine", "john", "albert", "merrita", "alphered", "sung", "lilia", "nidhi", "sarah", "joe", "jim", "calvert", "memphis"]

# All Functions

def page_break():
    print("---------------------------------------------------------------------------")

def user_cards():
    print(list_cards)

def action_print():
    print("You entered", card_enter, ".", opp1, "entered", opp1_card, ".", opp2, "entered", opp2_card)

def check_cards():
    if card_enter == opp1_card:
        if opp1_card == opp2_card:
            print("All of you entered the same card. No penalty.")
            action_print()
        elif opp1_card <= opp2_card:
            print(opp2, " wins that round.")
            action_print()
        elif opp1_card >= opp2_card:
            print("Nothing happens.")
            action_print()
        else:
            print("Okay!!")
    elif card_enter <=  opp1_card:
        if opp1_card == opp2_card:
            print(opp1, " and ", opp2, " entered the same cards. Nothing happens.")
            action_print()
        elif opp1_card <= opp2_card:
            print(opp2, " wins that round.")
            action_print()
        elif opp1_card >= opp2_card:
            print(opp1, " wins that round.")
            action_print()
        else:
            print("Okay!!")
    elif card_enter >= opp1_card:
        if opp1_card == opp2_card:
            print("You win")
            action_print()
        elif opp1_card <= opp2_card:
            if opp2_card == card_enter:
                print("You tied with someone.")
                action_print()
            elif opp2_card <= card_enter:
                print("You win.")
                action_print()
            elif opp2_card >= card_enter:
                print("You lost L")
                action_print()
            else:
                action_print()
        else:
            print("You won!!!")
            action_print()       
    else:
        print("bye")

# Code

# front - with instructions

print()
page_break()
print()
print("Welcome to the game of Bet the Highest Number. You will be given 6 cards to play with. Enter the highest number and compete against 2 players online.")
print()
time.sleep(2)
print("Please input only card numbers GIVEN. The game will kick you out if you try cheating.")
print()
time.sleep(2)
print("Have fun.")
page_break()
time.sleep(2)
print("Game is starting now.... Get ready")
time.sleep(2)

# Page 1 (after instructions)
page_break()
print("Here are your cards:")
user_cards1 = random.choice(card_pack) # 1st Card
print(user_cards1)
time.sleep(1)
user_cards2 = random.choice(card_pack) # 2nd Card
print(user_cards2)
time.sleep(1)
user_cards3 = random.choice(card_pack) # 3rd Card
print(user_cards3)
time.sleep(1)
user_cards4 = random.choice(card_pack) #4th card
print(user_cards4)
time.sleep(1)
user_cards5 = random.choice(card_pack) # 5th Card
print(user_cards5)
time.sleep(1)
user_cards6 = random.choice(card_pack) # 6th Card
print(user_cards6)
page_break()

    # Page 2
    # Opponents and Your Name

user_name = input("Enter your name: ").lower
opp1 = random.choice(opponent_names)
opp2 = random.choice(opponent_names)
    # Check if opp 1 = opp 2

if opp1 == opp2:
    opp2 = random.choice(opponent_names)
    if opp1 == opp2:
          opp2 = "patricia"
    else:
        c = opp2
else:
        c = opp2

    # Game Begins

time.sleep(1)

print("The game starts. You have 4 seconds to decide which card you would like to put down. The card with the highest value wins. The goal of the game is to have the highest amount of cards at the end.")
list_cards = [user_cards1, user_cards2, user_cards3, user_cards4, user_cards5, user_cards6]

while True:


    card_enter = input("Which card would you like to input: ")

    card_enter = int(card_enter)
    # Card FUnction
    if card_enter == user_cards1:
        print(user_cards1, " is being put in")
        list_cards.remove(user_cards1)
    elif card_enter == user_cards2:
        print(user_cards2, " is being put in")
        list_cards.remove(user_cards2)
    elif card_enter == user_cards3:
        list_cards.remove(user_cards3)
        print(user_cards3, " is being put in")
    elif card_enter == user_cards4:
        list_cards.remove(user_cards4)
        print(user_cards4, " is being put in")
    elif card_enter == user_cards5:
        print(user_cards5, " is being put in")
        list_cards.remove(user_cards5)
    elif card_enter == user_cards6:
        print(user_cards6, " is being put in")
        list_cards.remove(user_cards6)
    else:
        print("Invalid Card")
        print("Put a real card.")
        user_cards()
        card_enter = input("Which card would you like to input: ")
        card_enter = int(card_enter)
        if card_enter == user_cards1:
            print(user_cards1, " is being put in")
        elif card_enter == user_cards2:
            print(user_cards2, " is being put in")
        elif card_enter == user_cards3:
            print(user_cards3, " is being put in")
        elif card_enter == user_cards4:
            print(user_cards4, " is being put in")
        elif card_enter == user_cards5:
            print(user_cards5, " is being put in")
        elif card_enter == user_cards6:
            print(user_cards6, " is being put in")
        else:
            print("Invalid Card")
            print("Put a real card.")
            user_cards()
            card_enter = input("Which card would you like to input: ")
            card_enter = int(card_enter)
            if card_enter == user_cards1:
                print(user_cards1, " is being put in")
            elif card_enter == user_cards2:
                print(user_cards2, " is being put in")
            elif card_enter == user_cards3:
                print(user_cards3, " is being put in")
            elif card_enter == user_cards4:
                print(user_cards4, " is being put in")
            elif card_enter == user_cards5:
                print(user_cards5, " is being put in")
            elif card_enter == user_cards6:
                print(user_cards6, " is being put in")
            else:
                break
    
    opp1_card = random.choice(card_pack)
    opp2_card = random.choice(card_pack)
    time.sleep(2)
    check_cards()

    print("Your cards now:")
    print(list_cards)
    page_break()
    time.sleep(2)
