# In this part I will learn about "Generators"

""" Generators in Python are special type of functions that allow you to create an iterable sequence of values. 
    A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. 
    Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, 
    rather than having to create and store the entire sequence in memory. """

""" In Python, you can create a generator by using the yield statement in a function. 
    The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested. """

# Example :~~>

def my_generator():
    for i in range(1,7):
        yield f"Iteration {i} Value : {i}"

gen = my_generator()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

""" As you can see, the generator function my_generator() returns a generator object, which can be used to generate the values in the range 1 to 7. 
    The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function. """

# Now if you don't wanted to repeat the same statement then you can use looping statement as follow
for k in gen:
    print(k)

# Advantages (Benifits) of using Generators :~~>
""" Generators offer several benefits over other types of sequences, such as lists, tuples, and sets. 
    One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory. 
    This makes generators a powerful tool for working with large or complex data sets, as you can generate the values as you need them, rather than having to store them all in memory at once. """

""" Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested. 
    This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front. """

# Conclusion :~~>
""" Generators in Python are a powerful tool for working with large or complex data sets, allowing you to generate the values on-the-fly and store only what you need in memory. 
    Whether you are working with a large dataset, performing complex calculations, or generating a sequence of values, generators are a must-have tool in your programming toolkit. """