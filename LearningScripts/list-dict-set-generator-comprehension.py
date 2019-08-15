ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

ls = [i for i in range(100) if i%3==0]

print(ls)


dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
dict1 = {i:f"Item {i}" for i in range(5)}

dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)

dresses = [dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]]
print(type(dresses))

evens = (i for i in range(100) if i%2==0)
print(evens.__next__())
#
for item in evens:
    print(item)


#-----Exercise to practice--------

no_of_list = int(input("How many items add in a list: "))
input_string = input("Enter a list element separated by space ")
list = input_string.split()
t = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
if t==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {f'item{i}': i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s ={i for i in list}
    print(s)
    print(type(s))