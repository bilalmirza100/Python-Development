import random
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)

user_card = []
comp_card = []

for a in range(0, 2):
    user_card.append(deal_card())