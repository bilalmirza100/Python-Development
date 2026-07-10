import random
stages = ['''
  +---+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ['''
     _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''']
print(logo)
list = ["bilal", "mirza", "sadia", "ayesha", "kashaf", "zainab", "areeba", "hina", "sana", "aiman"]
random_name = random.choice(list)
lives = 6

display = []
for letter in range(len(random_name)):
    display += "_"
while "_" in display:
    guess = input("Guess a letter: ").lower()

    for letter in range(len(random_name)):
        if random_name[letter] == guess:
            display[letter] = guess
    if guess not in random_name:
        lives -= 1
        if lives == 0:
            print("You lose!")
            break
    print("Current progress:", " ".join(display))
    if "_" not in display:
        print("You win!")
        break
    print(stages[lives])