"""when you import a script in python, it will execute the whole script first, before allowing
its attributes to be accessible... that's why you should put your executable code wihin a main function
so that it does not run automatically if the file is imported elsewhere"""
import namemainexp1


print(namemainexp1.add(3,5))