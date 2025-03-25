# In this part I will learn about "Creating Command line Utility using python"

""" Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. 
    In Python, you can create your own command line utilities using the built-in argparse module. """

import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument("URL","URL of the File to Download")
parser.add_argument("output", help="by which name do you want to save your file")

args = parser.parse_args()

# Conclusion :~~>
""" Creating command line utilities in Python is a straightforward and flexible process thanks to the argparse module. 
    With a few lines of code, you can create powerful and customizable command line tools that can make your development workflow easier and more efficient. 
    Whether you're working on small scripts or large applications, the argparse module is a must-have tool for any Python developer. """