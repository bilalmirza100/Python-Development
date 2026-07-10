
from email.mime import message


alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
         shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
         position = alphabet.index(letter)
         new_position = position + shift_amount
         end_text += alphabet[new_position]
        else:
            end_text += letter 
    print(f"The {direction}d text is: {end_text}")
end = True
while end:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number:\n"))

    shift = shift % 26
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer == 'no':
        end = False
        print("Good Bye Buddy!")