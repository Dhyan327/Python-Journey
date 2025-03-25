# In this part I will learn about more types of string operation

a = "dhyan\n"        
print(a.islower())     # The islower function returns "true" only if all the character in the string are in lowercase, else it return "false" as an output
print(a.isprintable()) # The isprintable function returns "True" only if all the values within the given string are printabnle. If not, then return "False" as an output 
                       # Here, "\n" is not printable so it returns "False" as output

b = "       "          # Using spacebar
print(b.isspace())     # The isspace function returns "True" only and only if the string contains whitespaces, else returns "False" 
c = "       "          # Using Tab
print(c.isspace())     # The whitespaces is any string of text composed only of spaces, tabs, or line breaks

d = "Indian Institute Of Technology"
print(d.istitle())     # The istitle function returns "True" only if the first letter of each word of the string is capitalized, else it returns "False" as output
print(d.swapcase())    # The swapcase function changes the character casing i.e. Upper case are converted to lower case and Lower case are converted into Upper case.

e = "DHYAN"
print(e.isupper())     # The isupper function returns "true" only if all the character in the string are in uppercase, else it return "false" as an output