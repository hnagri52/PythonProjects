"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


"""

def missingNum(list):
    num = 0

    for item in list:
        if item < 0:
            pass




    return num



if __name__ == '__main__':
    print(missingNum([-1, -3, -4, -7, 0, 12,2,3,4,5,5,6]))