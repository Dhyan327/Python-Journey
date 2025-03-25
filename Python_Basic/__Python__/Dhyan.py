def welcome():
    print("Hey, you are welcome from Dhyan")
# welcome()

"""In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module.
   When a Python script is run directly, the __name__ variable is set to the string __main__. 
   When the script is imported as a module into another script, the __name__ variable is set to the name of the module.
"""
print(__name__)

if __name__ == "__main__":
    welcome()