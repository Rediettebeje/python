alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text,shift_amount):
    encrypted_text = ""


# inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
   # index()built in function, allows us to find out the position of an item in a list. e.g.
    # fruits = ["Apple", "Pear", "Orange"]
    # fruits.index("Pear") #1
    for letter in original_text:
        index_of_letter = alphabet.index(letter)
        new_position = index_of_letter + shift_amount
        encrypted_text += alphabet[new_position]
    print(encrypted_text)

# What happens if you try to shift z forwards by 9? Can you fix the code?


# Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# encrypt("hello",1)
encrypt(text,shift)