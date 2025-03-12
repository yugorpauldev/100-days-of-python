import random

def play_game(): 
    def deal_card():
        
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        new_card = random.choice(cards)

        return new_card

    user_deck = []
    computer_deck = []
    is_game_over = False

    def calculate_score(something):
        if sum(something) == 21 and len(something) == 2:
            return 0  

        if 11 in something and sum(something) > 21:
            something.remove(11)
            something.append(1)
        
        return sum(something)


    def compare(user_score, computer_score):
        if user_score == computer_score:
            print("It's a Draw")
        elif computer_score == 0:
            return "Lose, opponet has Blackjack"
        elif user_score == 0:
            return "Win with a BlackJack"
        elif user_score > 21:
            return "You went over, you lose"
        elif computer_score > 21:
            return "Opponent went over, You win"
        elif user_score > computer_score:
            return "You win"
        else:
            return "You Lose"

        
        
    for i in range(2):
        user_deck.append(deal_card())
        computer_deck.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)
        print(f"    Your cards: {user_deck}, current score: {user_score}")

        print(f"    Computer's first card: {computer_deck[0]}")
        

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            decision = input("Type 'y' to get another card,type 'n' to pass:")
            if decision == "y":
                user_deck.append(deal_card())
            else:
                is_game_over = True


                
    while computer_score !=0 and computer_score < 17:
        computer_deck.append(deal_card())
        computer_score = calculate_score(computer_deck)

    print(f" Your final hand:{user_deck}, final score: {user_score}")
    print(f" Computer's final hand: {computer_deck}, final_score: {computer_score}")
    print(compare(user_score,computer_score))
           
while input("Would you like to Play BlackJack game?\nType 'y' if Yes and 'n' if no: ") == "y":
    play_game()    
    

