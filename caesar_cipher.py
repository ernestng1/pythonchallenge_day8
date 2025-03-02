from operator import truediv
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
continue_caesar = True

def caesar(encrypt_or_decrypt, original_text, shift_amount):
    caesar_text = ""
    if encrypt_or_decrypt == "encode":
        shift_amount *= 1
    elif encrypt_or_decrypt == "decode":
        shift_amount *= -1

    for i in original_text:
        if i.lower() in alphabet:
            caesar_text += alphabet[((alphabet.index(i))+shift_amount)%len(alphabet)]
        else:
            caesar_text += i
    print(f"Here is the {encrypt_or_decrypt}d result: {caesar_text}")

    ask_continue_caesar = input("Write 'Yes' if you would still want to decode/encode, 'No' if you want to stop:\n")

    return caesar_text, ask_continue_caesar.lower()

while continue_caesar == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    values_to_capture = caesar(original_text=text, shift_amount=shift, encrypt_or_decrypt=direction)

    if values_to_capture[1] == "no":
        continue_caesar = False
        print("Goodbye")