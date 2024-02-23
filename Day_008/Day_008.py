alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caeser(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=letter      
    print(f"The {cipher_direction}d text is {end_text}") 

from art import logo
print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%(len(alphabet)-1)

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text,shift_amount):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     cipher_text = ""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position+shift_amount
#         if new_position>len(alphabet):
#             new_position=position+shift-len(alphabet)
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text}")
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         if new_position<0:
#             new_position=position-shift+len(alphabet)
#         new_letter=alphabet[new_position]
#         plain_text+=new_letter
#     print(f"The decoded text is {plain_text}")    
#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction=='encode':
#     encrypt(plain_text=text, shift_amount=shift)  
# elif direction=='decode':
#     decrypt(cipher_text=text, shift_amount=shift) 
# else:
#     print("Choose encode or decode")

    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
