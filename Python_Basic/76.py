# In this part I will learn about "Regular Expression"

""" Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. 
    They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code. """
# In Python, regular expressions are supported by the re module.

# Metacharacters in regular expressions :~~>
""" 
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the charactersseparated by it.)
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs """
# Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions 

# re.search() Method :-->
""" re.search() method either returns None (if the pattern doesnt match), or a re.MatchObject that contains information about the matching part of the string. 
    This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. 
    We can use re.search method like this to search for a pattern in regular expression: """

import re

txt1 = '''  What is Python? It is a programming language that is interpreted, object-oriented, and considered to be high-level too. 
        The Python is one of the easiest yet most useful programming languages which is widely used in the software industry. 
        People use Python for Competitive Programming, Web Development, and creating software. 
        Its demand is growing at a very rapid pace due to its vast use cases in Modern Technological fields like Data Science, Machine learning, AI and Automation Tasks.  '''

pattern1 = "AI"
match1 = re.search(pattern1, txt1)
print(match1)
print()

# re.finditer() Method :-->
pattern2 = r"[P]+ython"                 # Here, we can also write only "Python", both are same.
match2 = re.finditer(pattern2, txt1)
print(match2)

for i in match2:
    print(i)
print()

txt2 = '''  Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. 
        Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. 
        It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. 
        Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 
        1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). '''

# re.findall() Method :-->
pattern3 = r"[A-Z]+yclone"
match3 = re.findall(pattern3, txt2)
print(match3)
print()

# re.sub() Method (Replacing a pattern) :-->
txt3 = "The cat is in the hat."

pattern4 = r"[a-z]+at"
matches = re.findall(pattern4, txt3)
print(matches)                          # Output: ['cat', 'hat']

new_text = re.sub(pattern4, "dog", txt3)
print(new_text)                         # Output: "The dog is in the dog."
print()

# Extracting information from a string :-->
txt4 = "The email address is example@example.com."
pattern5 = r"\w+@\w+\.\w+"
match = re.search(pattern5, txt4)

if match:
    email = match.group()
    print(email)                # Output: example@example.com

# For going deep into regular expression do refer this website - https://regexr.com/

# Conclusion :~~>
""" Regular expressions are a powerful tool for working with strings and text data in Python. 
    Whether you're matching patterns, replacing text, or extracting information, 
    regular expressions make it easy to perform complex string operations with just a few lines of code. """