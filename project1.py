import random
import time

# --- Game Data (Nested Dictionaries) ---
game_data = {
    "player": {
        "name": "Soldier",
        "hp": 150,
        "max_hp": 150,
        "attack": 25,
        "heal_potions": 3
    },
    "enemies": [
        {"name": "Goblin Scout", "hp": 40, "attack": 10},
        {"name": "Goblin Warrior", "hp": 50, "attack": 12},
        {"name": "Orc Berserker", "hp": 80, "attack": 18},
        {"name": "Orc Warchief", "hp": 100, "attack": 22},
        {"name": "Ancient Dragon (BOSS)", "hp": 180, "attack": 30}
    ]
}

def display_stats(player, enemy):
    print("\n" + "="*40)
    print(f" {player['name']} (HP: {player['hp']}/{player['max_hp']}) | Potions: {player['heal_potions']}")
    print(f" VS ")
    print(f" {enemy['name']} (HP: {enemy['hp']})")
    print("="*40)

def player_turn(player, enemy):
    while True:
        print("\nAapka turn hai! Kya karna chahenge?")
        print("1. Attack ⚔️")
        print("2. Heal 🧪")
        choice = input("Option select karein (1 ya 2): ")

        if choice == '1':
            damage = random.randint(player['attack'] - 5, player['attack'] + 5)
            enemy['hp'] -= damage
            print(f"\n💥 Aapne {enemy['name']} par attack kiya aur {damage} damage diya!")
            break
        elif choice == '2':
            if player['heal_potions'] > 0:
                heal_amount = 40
                player['hp'] = min(player['max_hp'], player['hp'] + heal_amount)
                player['heal_potions'] -= 1
                print(f"\n🧪 Aapne potion pi li! 40 HP restore hui. Current HP: {player['hp']}")
                break
            else:
                print("\n❌ Aapke paas potions khatam ho chuki hain!")
        else:
            print("\n❌ Invalid choice! Sahi option chunein.")

def enemy_turn(player, enemy):
    if enemy['hp'] > 0:
        print(f"\n🔄 {enemy['name']} ki turn hai...")
        time.sleep(1)
        damage = random.randint(enemy['attack'] - 3, enemy['attack'] + 3)
        player['hp'] -= damage
        print(f"🔥 {enemy['name']} ne aap par attack kiya aur {damage} damage diya!")

def battle(player, enemy):
    print(f"\n⚠️ Ek jungli {enemy['name']} samne aaya!")
    
    while player['hp'] > 0 and enemy['hp'] > 0:
        display_stats(player, enemy)
        
        player_turn(player, enemy)
        
        if enemy['hp'] <= 0:
            print(f"\n🎉 Aapne {enemy['name']} ko hara diya!")
            # Match jeetne par thodi HP recovery aur reward
            player['hp'] = min(player['max_hp'], player['hp'] + 20)
            player['heal_potions'] += 1
            print(f"🎁 Bonus: Aapki 20 HP restore hui aur 1 Potion mili!")
            return True
            
        enemy_turn(player, enemy)
        
        if player['hp'] <= 0:
            print("\n💀 Aap jung mein mare gaye... GAME OVER!")
            return False

def start_game():
    player = game_data['player']
    enemies = game_data['enemies']
    
    print("⚔️ WELCOME TO THE SOLDIER'S QUEST ⚔️")
    print("You have to defeat 5 dangerous enemies. Best of luck!")
    
    for index, enemy in enumerate(enemies):
        print(f"\n--- ROUND {index + 1} ---")
        
        won = battle(player, enemy)
        
        if not won:
            break
    else:
        print("\n🏆 CONGRATULATIONS! You have defeated the dragon! 🏆")

start_game()