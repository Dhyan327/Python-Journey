# In this part I will learn about "MultiProcessing using Python"

# 1st Method (using Multiprocessing  Module) :-->
""" Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel. 
    It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code.  """

""" Now, to do multiprocessing we need to create a process object which calls a start() method. 
    The start() method runs the process and then to stop the execution, we use the join() method. Here's how we can create a simple process. """

""" The following are some of the most commonly used functions in the multiprocessing module:
    1) multiprocessing.Process(target, args): This function creates a new process that runs the target function with the specified arguments.
    2) multiprocessing.Pool(processes): This function creates a pool of worker processes that can be used to parallelize the execution of a function across multiple input values.
    3) multiprocessing.Queue(): This function creates a queue that can be used to communicate data between processes.
    4) multiprocessing.Lock(): This function creates a lock that can be used to synchronize access to shared resources between processes. """

import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started Downloading file{name}")
    response = requests.get(url)
    open(f"Files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading file{name}")

if __name__ == "__main__":
    url = "https://picsum.photos/1920/1080"                 # This url will generate random pictures every time it runs.
    process = []

    for i in range(1,6):
        # downloadFile(url, i)                              # Normal Way
        p = multiprocessing.Process(target=downloadFile, args=[url,i])
        p.start()
        process.append(p)

    for i in process:
        i.join()
    print()

# Note :~~>
""" In Windows, the child process needs to import the __main__ module before it can start executing. 
    This means that you need to use the if __name__ == '__main__': idiom to ensure that the child processes don't execute the main module's code when they are spawned. 
    So, Make sure to include this if __name__ == '__main__': guard in your script. 
    This ensures that the multiprocessing code is only executed when the script is run directly, not when it's imported as a module. """


# 2nd Method (using concurrent.futures  Module) :-->
from concurrent.futures import ProcessPoolExecutor

def FileDownload(url, name):
    print(f"Started Downloading file{name}")
    response = requests.get(url)
    open(f"file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading file{name}")
    return f"file{name}.jpg downloaded successfully"

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        names = [i for i in range(1,6)]
        urls = [url for _ in range(1, 6)]
        results = executor.map(FileDownload, urls, names)
        for r in results:
            print(r)

# Conclusion :~~>
""" As you can see, the multiprocessing module provides a simple and efficient way to run multiple processes in parallel. 
    Whether you need to create a new process, run a function across multiple input values, communicate data between processes, 
    or synchronize access to shared resources, the multiprocessing module has you covered.

    In conclusion, the multiprocessing module is a powerful tool for parallelizing code in Python. 
    Whether you are a beginner or an experienced Python developer, the multiprocessing module is an essential tool to have in your toolbox. """