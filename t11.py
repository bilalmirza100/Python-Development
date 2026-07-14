import random
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)
def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, Opponent has Blackjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif comp_score > 21:
        return "Opponent went over, You Win"
    elif user_score > comp_score:
        return "You Win"
    else:
         return "You Win" 
def play_game():
    user_card = []
    comp_card = []
    is_game_over = False

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return  sum(cards)

    for a in range(0, 2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_card)
        comp_score = calculate_score(comp_card)
        print(f"Your Cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_card.append(deal_card())
        comp_score = calculate_score(comp_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {comp_card}, final score: {comp_score}")
    print(compare(user_score, comp_score))

    while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
        play_game()
play_game()