
def ThresholdSelector():
    #answering the following examples
    """
    (list of number, int) -> list of number

    Return a new list consisting of those numbers in nums

    that are below threshold,

    in the same order as in nums.

    >>> collect_underperformers([1, 2, 3, 4], 3)

    [1, 2]

    >>> collect_underperformers([1, 2, 108, 3, 4], 50)

    [1, 2, 3, 4]

    """
    #defining the function
    def collect_underperformers(n,thres):
        #Initialize an empty list
        outlist = list()
        #loops the following code until it hits the length of n
        for i in range(0, len(n)):
            #checks whether the value is less than the threshold
            if n[i]<thres:
                #if the number is less than the value of thres, append it to "outlist")
                outlist.append(n[i])
        #after the loop is finish, print out the new list
        print (outlist)
        #example
    n=[5,6,7,8,9,1,3,4,5,2,5]
    thres=7
    print (collect_underperformers(n,thres))


ThresholdSelector()

