"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""
from collections import deque

def sumChecker(numList, k):
    mainList = numList
    temp = numList.copy()
    temp.pop(0)
    check = False


    for num in mainList:
        for random in temp:
            if (num + random) == k:
                check = True
                print("rumi")
        if len(temp) == 0:
            break
        temp.pop(0)


    return check


def main():
    print(sumChecker([10, 15, 3, 7], 17))

if __name__ == '__main__':
    main()


