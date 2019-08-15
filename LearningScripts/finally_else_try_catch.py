f1 = open("huss.txt")
try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error: ", e)

except IOError as e:
    print("Print IO error: ", e)

else:
    print("This will run only if except is not running")
#this is run no matter what! it is used to do things we must do. For example, we may be connected to a remote data center through the network or working with a file or working with a Graphical User Interface (GUI).
finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")

