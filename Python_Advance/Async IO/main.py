# In this part I will learn about "Async IO in Python"

""" Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. 
    In Python, async programming is achieved through the use of the asyncio module and asynchronous functions. """

# Example :~~>
import asyncio
import time
import requests

async def func1():
    await asyncio.sleep(2)
    print("Func1 executed successfully!")

async def func2():
    await asyncio.sleep(1)
    print("Func2 executed successfully!")

async def func3():
    await asyncio.sleep(5)
    print("Func3 executed successfully!")

async def main1():
    ask = asyncio.create_task(func1())           # This means that "func1()" will be executed whenever it gets interval
    # await func1()
    await func2()
    await func3()
    print()
asyncio.run(main1())

# Real World Example :~~>

async def myfunc1():
    print("MyFunc1 executed successfully!")
    URL = "https://as1.ftcdn.net/v2/jpg/06/38/88/92/1000_F_638889295_ZWN7yMVzo4JRdaqgN1IFZsvNGlUhnrw3.jpg"
    response = requests.get(URL)
    open("img1.jpg", "wb").write(response.content)

async def myfunc2():
    print("MyFunc2 executed successfully!")
    URL = "https://as1.ftcdn.net/v2/jpg/06/27/32/78/1000_F_627327855_qofxDgXea4mG811FSIkBXuCae9ADQg94.jpg"
    response = requests.get(URL)
    open("img2.jpg", "wb").write(response.content)

async def myfunc3():
    print("MyFunc3 executed successfully!")
    URL = "https://as1.ftcdn.net/v2/jpg/06/58/62/40/1000_F_658624012_GoPgap4BYNaZzRigFtu42wJU1if9IjE6.jpg"
    response = requests.get(URL)
    open("img3.jpg", "wb").write(response.content)

async def myfunc4():
    print("MyFunc4 executed successfully!")
    URL = "https://as1.ftcdn.net/v2/jpg/07/45/41/42/1000_F_745414276_psGJogUYrDD59cknXto4S9joa2LKwuZv.jpg"
    response = requests.get(URL)
    open("img4.jpg", "wb").write(response.content)

async def myfunc5():
    print("MyFunc5 executed successfully!")
    URL = "https://as2.ftcdn.net/v2/jpg/06/27/32/77/1000_F_627327742_qvj9BLTQe8XqjTZYounjLKmU2z73PT0e.jpg"
    response = requests.get(URL)
    open("img5.jpg", "wb").write(response.content)

async def main2():
    L = await asyncio.gather(
        myfunc1(),
        myfunc2(),
        myfunc3(),
        myfunc4(),
        myfunc5(),
    )
    print(L)                                    # This will print the return value of each function
asyncio.run(main2())

# Conclusion :~~>
""" Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python. 
    With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread. 
    Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer. """