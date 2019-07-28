


def func(var, *letters, **roles):
    """This function is used to learn and print different arguments entered"""
    print(f"\n\nthe variable you entered is {var}")

    print("\n\nThis is all of the entries in the list/range of variables entered:")
    if not letters:
        print("The list is empty or there were no multiple params passed")
    for letter in letters:
        print(letter)

    print("\n\nThis is all of the entries in the dictionary:")
    if not roles:
        print("dict is empty")
    for key, value in roles.items():
        print(f"This is the key: {key} and this is its value: {value}")


name = "Hussein"
mylist = ["Hussein", ["Huss", "SABS"], (1,2,3) , "done"]
mydict = {"Hussein": "Plumber", "Sab" : "Nurse", "momo" : "doctor"}

func(name, "hihi", "HUssein, Bbubs", ["sabs, husse"])

func(name, **mydict)