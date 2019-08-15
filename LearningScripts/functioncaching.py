"""The purpose of function caching is to avoid waitinf for some processes.
It is used when the function will be called multiple times with the same parameters
But the process takes too long. So we store the return value, and do it right away"""
import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")


#asking the user how many values they want to cache
from functools import lru_cache
import time
@lru_cache(maxsize=(int(input("How many values would you like to cache = "))))
def funccc():
    time.sleep(5)


if __name__ == '__main__':
    print("Loading your game:")
    funccc()
    print("File not found")
    funccc()
    print("Loading again")
    funccc()
    print("Done")