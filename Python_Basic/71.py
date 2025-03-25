# In this part I will learn about "Time Module"

""" The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. 
    This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications.  """

# time.time() :~~>
""" The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch.
    The epoch is the point where the time starts and is platform-dependent. On Windows and most Unix systems, the epoch is January 1, 1970, 00:00:00 (UTC)"""

# Example :~~>
import time
print(time.time())
print()

def usingWhile():
	i = 0
	while i<50000:
		i = i +1 
		
def usingFor():
	sum = 0
	for i in range(50000):
		sum = sum + 1

init = time.time()
usingWhile()
t1 = time.time() - init
init = time.time()
usingFor()
t2 = time.time() - init
print(f"Time taken by While loop is {round(t1,3)}")
print(f"Time taken by For loop is {round(t2,3)}")
print()

# time.sleep()	:~~>
""" The time.sleep() function suspends the execution of the current thread for a specified number of seconds. 
	This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads.  """

print("Start:", time.time())
time.sleep(3)
print("This statement is printed after 3 seconds.")
print("End:", time.time())
print()

# time.strftime()	:~~>
""" The time.strftime() function formats a time value as a string, based on a specified format. 
	This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report. """

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)

# Conclusion  :~~>
""" The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. 
	Whether you are writing a script, a library, or an application, the time module is a powerful tool that can help you perform time-related tasks with ease and efficiency. 
	So, if you haven't already, be sure to check out the time module in Python and see how it can help you write better, more efficient code. """