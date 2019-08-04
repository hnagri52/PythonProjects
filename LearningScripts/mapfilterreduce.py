

ls = ["1", "22", "444", "54540"]

for i in range(len(ls)):
    ls[i] = int(ls[i]) + 5

for item in ls:
    print(item)


#The map function will apply a function



ls2 = ["1", "22", "444", "54540"]
ls2 = list(map(int,ls))
print(ls)


#Now let's try map functinos with lamda LOL


ls3 = ["1", "22", "444", "54540"]
ls3 = list(map(lambda x:int(x)*int(x), ls3))
print(ls3)


#Something more complicated:

ls4 =  ["1", "22", "444", "54540"]

def square(a):
    return a*a
def cube(a):
    return a*a*a

func = [square,cube]

for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)


#//////////////////////////filter functions://///////////////////////////////////////////////

ls5 = [233,3,4,5,4,565,7,65,45]

def is_greater_than_5(a):
    return a>5

greater_than_5 = list(filter(is_greater_than_5, ls5))


print(greater_than_5)


#//////////////////////////REDUCE functions://///////////////////////////////////////////////

from functools import reduce

#you can do this
#num = 0
#for item in list:
#num = num + item


ls6 =  ["1", "22", "444", "54540"]

ans = reduce(lambda x,y:int(x)+int(y), ls6)
print(ans)









