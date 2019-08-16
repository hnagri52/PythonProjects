import os
print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("huss.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("huss.txt", "hussy.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/huss.txt"))
#
# # print(os.path.exists("C://Program Files2"))
# print(os.path.isfile("C://Program Files"))


with open("huss.txt") as f:
    filelist = f.read()
    print(filelist)
    filelist = filelist.split("\n")

print(filelist)
