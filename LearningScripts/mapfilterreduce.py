

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