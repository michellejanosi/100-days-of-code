alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encoded_text = ""

    for letter in text:
        position = alphabet.index(letter)
        encode_position = position + shift
        encoded_text += alphabet[encode_position]
  
    print(f"Your encoded text is: {encoded_text}")

def decode(text, shift):
    decoded_text = ""

    for letter in text:
        position = alphabet.index(letter)
        decode_position = position - shift
        decoded_text += alphabet[decode_position]
  
    print(f"Your decoded text is: {decoded_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decode(text, shift)