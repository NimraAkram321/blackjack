import random
from art import logo
import os
def deal_card():
  cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  return random.choice(cards) 
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards):
  if sum(cards) == 21 and len(cards)==2:
    return 0;
  elif sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  return sum(cards)
  

def campare_cards(user_score,computer_score):
  if user_score == computer_score :
    return "draw"
  elif user_score == 0:
    return " lose, opponent has balckjack"
  elif computer_score == 0:
    return "win with a blackjack"
  elif user_score > 21:
    return " You went over, you lose"
  elif computer_score > 21:
    return " Opponent went over , you win"
  elif user_score > computer_score:
    return " You Win"
  else:
    return "You lose"
def play():    
    user_cards = []
    computer_cards = []
    is_game_over=False;
    for  _ in range(2):
        user_cards.append(deal_card());
        computer_cards.append(deal_card())

    print(logo)
    while  not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f" Your cards : {user_cards}, current score : {user_score}")
        print(f" Computer's first card : {computer_cards[0]}")
        if user_score ==0 or computer_score == 0 or user_score >21:
            is_game_over=True
            
        else:
            draw_card=input("Type 'y' to get another card, type 'n' to pass :").lower()
            if(draw_card=='y'):
                user_cards.append(deal_card())
            
            else:
                is_game_over=True
    
    
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card());
        computer_score=calculate_score(computer_cards);

    print(f" Your final hand : {user_cards}, final score: {user_score} ")
    print(f" Computer's final hand : {computer_cards}, final score: {computer_score}")
    print(campare_cards(user_score,computer_score))

while input(" Do you want to play the game of Blackjack ? Type 'y' or 'n' ").lower() == "y":
  
  os.system('cls');
  play();