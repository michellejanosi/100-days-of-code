from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    result = ""

    if direction == 'decode':
            shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            result += alphabet[new_position]
        else:
            result += char
    
    print(f"Your {direction}d text is: '{result}'")

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    caeser(text, shift, direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
    if go_again == 'no':
        should_continue = False
        print("Goodbye")