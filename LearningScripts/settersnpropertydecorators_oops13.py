class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@hussy.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

#use a decorator change the function email into a property instead.. so dont have to call as function
    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@hussy.com"
#must use decorator to still set the email
    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

#we also need to create a custom decorator to delete the property

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


Huss= Employee("Hussein", "Nagri")

print(Huss.email)

Huss.fname = "US"

print(Huss.email)
Huss.email = "this.that@hussy.com"
print(Huss.fname)

del Huss.email
print(Huss.email)
Huss.email = "Harry.Perry@hussy.com"
print(Huss.email)