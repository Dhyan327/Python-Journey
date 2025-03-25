# In this part I will learn about "MultiThreading using Python"

""" Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. 
    In Python, we can use the threading module to implement multithreading. """

# 1st Method (using Threading Module) :-->

""" The following are some of the most commonly used functions in the threading module:
    1)  threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.
    2)  threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads. """

""" To create a thread, we need to create a Thread object and then call its start() method. 
    The start() method runs the thread and then to stop the execution, we use the join() method. Here's how we can create a simple thread. """

import threading
import time

def myfunc(sec):
    print(f"Sleeping for {sec} seconds!")
    time.sleep(sec)
    return F"Seconds : {sec}"

# myfunc(5)
# myfunc(3) 
# myfunc(2)

def main():
    time1 = time.perf_counter()

    threat1 = threading.Thread(target=myfunc, args=[3])
    threat2 = threading.Thread(target=myfunc, args=[2])
    threat3 = threading.Thread(target=myfunc, args=[1])

    threat1.start()
    threat2.start()
    threat3.start()

    threat1.join()
    threat2.join()
    threat3.join()

    time2 = time.perf_counter()
    print(f"Time Taken : {round(time2-time1,3)} seconds")
    print()
main()

# 2nd Method (using concurrent.futures Module) :-->

from concurrent.futures import ThreadPoolExecutor

def PoolingDemo1():                         # With "Submit" Method
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(myfunc, 3)
        future2 = executor.submit(myfunc, 2)
        future3 = executor.submit(myfunc, 1)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        print()

def PoolingDemo2():                     # With "map" Function
    with ThreadPoolExecutor() as executor:
        lst = [3,2,1]
        results = executor.map(myfunc, lst)
        for result in results:
            print(result)

PoolingDemo1()
PoolingDemo2()

# Conclusion :~~>
""" As you can see, the threading module provides a simple and efficient way to implement multithreading in Python. 
    Whether you need to create a new thread, run a function across multiple input values, or synchronize access to shared resources, the threading module has you covered.

    In conclusion, the threading module is a powerful tool for parallelizing code in Python. 
    Whether you are a beginner or an experienced Python developer, the threading module is an essential tool to have in your toolbox. 
    With multithreading, you can take advantage of multiple CPU cores and significantly improve the performance of your code. """   