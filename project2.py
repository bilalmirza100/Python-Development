import os
import random

SUITS = ('♠', '♥', '♦', '♣')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        self.reset()

    def reset(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            self.reset()
            self.shuffle()
            return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def get_value(self):
        self.adjust_for_ace()
        return self.value

    def clear(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])


class Chips:
    def __init__(self, filename="chips.txt", default_balance=500):
        self.filename = filename
        self.default_balance = default_balance
        self.total = self.load_chips()
        self.current_bet = 0

    def load_chips(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    content = file.read().strip()
                    if content.isdigit():
                        return int(content)
            except Exception:
                pass
        return self.default_balance

    def save_chips(self):
        try:
            with open(self.filename, 'w') as file:
                file.write(str(self.total))
        except Exception as e:
            print(f"\n[Warning] Chips save nahi ho sake: {e}")

    def place_bet(self, amount):
        if amount <= self.total:
            self.current_bet = amount
            self.total -= amount
            return True
        return False

    def win_bet(self):
        self.total += self.current_bet * 2
        self.current_bet = 0
        self.save_chips()

    def lose_bet(self):
        self.current_bet = 0
        self.save_chips()

    def push(self):
        self.total += self.current_bet
        self.current_bet = 0
        self.save_chips()

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.chips = Chips()
        
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def get_valid_bet(self):
        while True:
            try:
                print(f"\n💰 Aapka Current Balance: Rs. {self.chips.total}")
                bet_input = input("Bet lagayein (ya exit ke liye 'q' likhein): ").strip()
                
                if bet_input.lower() == 'q':
                    return None
                
                bet_amount = int(bet_input)
                
                if bet_amount <= 0:
                    print("❌ Bet hamesha 0 se barhi honi chahiye!")
                    continue
                
                if self.chips.place_bet(bet_amount):
                    return bet_amount
                else:
                    print("❌ Aapke paas itne paise nahi hain!")
            except ValueError:
                print("❌ Invalid Input! Meherbani karke sirf numbers (integers) type karein.")

    def show_table(self, hide_dealer_card=True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 55)
        print("🃏  OOP BLACKJACK CASINO SIMULATOR  🃏".center(55))
        print("=" * 55)
        
        if hide_dealer_card:
            visible_card = str(self.dealer_hand.cards[0])
            print(f"🕵️  DEALER HAND : [ {visible_card}, 🎴 Hidden ]  (Value: {VALUES[self.dealer_hand.cards[0].rank]})")
        else:
            print(f"🕵️  DEALER HAND : [ {self.dealer_hand} ]  (Value: {self.dealer_hand.get_value()})")
            
        print("-" * 55)
        
        print(f"👤  PLAYER HAND : [ {self.player_hand} ]  (Value: {self.player_hand.get_value()})")
        print("-" * 55)
        print(f"💵 Active Bet: Rs. {self.chips.current_bet}  |  💳 Wallet: Rs. {self.chips.total}")
        print("=" * 55)

    def play_round(self):
        self.player_hand.clear()
        self.dealer_hand.clear()
        
        self.deck.shuffle()

        bet = self.get_valid_bet()
        if bet is None:
            return False 

        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        self.show_table(hide_dealer_card=True)

        player_bust = False
        while self.player_hand.get_value() < 21:
            choice = input("\nKya aap 'Hit' karna chahte hain ya 'Stand'? (h/s): ").strip().lower()
            if choice == 'h' or choice == 'hit':
                self.player_hand.add_card(self.deck.deal_card())
                self.show_table(hide_dealer_card=True)
            elif choice == 's' or choice == 'stand':
                break
            else:
                print("Invalid input! Meherbani karke 'h' ya 's' likhein.")

        if self.player_hand.get_value() > 21:
            player_bust = True

        if not player_bust:
            while self.dealer_hand.get_value() < 17:
                self.dealer_hand.add_card(self.deck.deal_card())

        self.show_table(hide_dealer_card=False)

        player_score = self.player_hand.get_value()
        dealer_score = self.dealer_hand.get_value()

        if player_bust:
            print("\n💥 Aww! Aap BUST ho gaye (21 se upar). Dealer jeet gaya!")
            self.chips.lose_bet()
            self.losses += 1
        elif dealer_score > 21:
            print("\n🎉 Dealer BUST ho gaya! Aap JEET gaye! 🥳")
            self.chips.win_bet()
            self.wins += 1
        elif player_score > dealer_score:
            print(f"\n🎉 Aapke points ({player_score}) Dealer ({dealer_score}) se zyada hain. Aap JEET gaye!")
            self.chips.win_bet()
            self.wins += 1
        elif player_score < dealer_score:
            print(f"\n📉 Dealer ({dealer_score}) ke points aap ({player_score}) se zyada hain. Aap HAAR gaye!")
            self.chips.lose_bet()
            self.losses += 1
        else:
            print(f"\n🤝 Match Draw (Push)! Dono ka score {player_score} hai. Aapke paise wapas.")
            self.chips.push()
            self.ties += 1

        input("\nAgle round ke liye 'Enter' dabayein...")
        return True

    def show_final_report(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 55)
        print("📊  FINAL CASINO REPORT CARD  📊".center(55))
        print("=" * 55)
        print(f"🏆 Total Wins   : {self.wins}")
        print(f"❌ Total Losses : {self.losses}")
        print(f"🤝 Ties / Pushes: {self.ties}")
        print(f"💰 Final Chips  : Rs. {self.chips.total}")
        
        net_profit = self.chips.total - self.chips.default_balance
        if net_profit > 0:
            print(f"📈 Profit       : +Rs. {net_profit} (Kasino ko loot liya!) 😎")
        elif net_profit < 0:
            print(f"📉 Loss         : Rs. {abs(net_profit)} (Aaj kismat kharab thi!) 😢")
        else:
            print("⚖️ No Profit, No Loss (Barabar rahe).")
        print("=" * 55)
        print("Khelne ka shukriya! Dobara aaiyega. 👋")


if __name__ == "__main__":
    game = BlackjackGame()
    print("💎 Welcome to the High-Stakes Blackjack Table! 💎")
    
    playing = True
    while playing:
        if game.chips.total <= 0:
            print("\n❌ Oh no! Aapke paas bilkul chips khatam ho chuke hain!")
            reset_choice = input("Kya aap apna wallet Rs. 500 se reload karna chahte hain? (y/n): ").strip().lower()
            if reset_choice == 'y':
                game.chips.total = 500
                game.chips.save_chips()
                continue
            else:
                break
        
        playing = game.play_round()

    game.show_final_report()