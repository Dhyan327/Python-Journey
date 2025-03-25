# In this part I will do "Exercise 4 Solution"

# Exercise :-->
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Encoding:
""" if the word contains atleast 3 characters, remove the first letter and append it at the end
   now append three random characters at the starting and the end
   else simply reverse the string"""

# Decoding:
""" if the word contains less than 3 characters, reverse it
    else remove 3 random characters from start and end. Now remove the last letter and append it to the beginning"""

# Solution :~~>

import random
import string

def generate_random_characters(n=3):
    return ''.join(random.choices(string.ascii_letters, k=n))

def encode_word(word):
    if len(word) < 3:
        return word[::-1]
    first_char = word[0]
    transformed_word = word[1:] + first_char
    random_prefix = generate_random_characters(3)
    random_suffix = generate_random_characters(3)
    return random_prefix + transformed_word + random_suffix

def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    core_word = word[3:-3]
    last_char = core_word[-1]
    original_word = last_char + core_word[:-1]
    return original_word

choice = input("Enter 1 for Encoding Message\nEnter 2 for Decoding Message\nEnter your Choice : ")

word = input("Enter your Message : ")
if choice == "1":
    encod = encode_word(word)
    print(f"Encoded Message : {encod}")

elif choice == "2":
    decod = decode_word(word)
    print(f"Decoded Message : {decod}")

else:
    print("Please Enter a Valid Choice!")