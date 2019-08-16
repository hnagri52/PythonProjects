"""Will take a path, file, and the format to replace, and clean up the folder"""
import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

soldier(r"C:\Users\Hussein\Desktop\FrontendLearning",
        r"C:\Users\Hussein\PycharmProjects\PythonLearning\files.txt", ".jpg" )

