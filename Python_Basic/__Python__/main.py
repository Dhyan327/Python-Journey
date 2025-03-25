# In this part I will learn about {if __name__ == "__main__" statement} in python.

""" The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script."""

import Dhyan
Dhyan.welcome()

"""It's important to note that the if __name__ == "__main__" idiom is not required to run a Python script.
   You can still run a script without it by simply calling the functions or running the code you want to execute directly.
   However, the if __name__ == "__main__" idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module."""