"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""

def sort(list):

    newlist = []
    temp = 1

    for index, num in enumerate(list):
        for index2, num2 in enumerate(list):
            if (index == index2):
                continue

            temp *= num2
        newlist.append(temp)
        temp = 1



    return newlist




if __name__ == '__main__':
    print(sort([1, 2, 3, 4, 5]))
