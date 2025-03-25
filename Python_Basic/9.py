# In this part I will learn about more types of string operation

# The capitalize method will turn only the first letter of the string in uppercase and the rest of the character in lowercase
a = "introduction to Python"   # Here, 'i' of introduction will turn into capital "I" and 'P' of python will turn smaller i.e. "p" 
print(a.capitalize())          # The string will have no effect if the first character is already in uppercase

print(a.center(50))       # The centre method will allign the string to the centre as per the parametre given by the user 
print(len(a))
print(len(a.center(50)))
print(a.center(50,"_"))   # This code will add the "_" line before and after the string 
print(a.title())          # The title function capitalize each first letter of the word within the string 
print("\n")

b = "IntroductionToPython" # The isalnum function returns true only if the entire string only consist of A-Z, a-z, 0-9.
print(b.isalnum())   # If any other characters or punctuation are present, them it returns false as output. If there is space between two character then also it returns "false" 

print(b.isalpha())   # The isalpha function returns true only if the entire string only consist of A-Z, a-z. 
                     # If any other characters or punctuation or number(0-9) are present, them it returns false as output