class Dad:
    job = 1


class Son(Dad):
    dance = 1

    job = 2

    def is_dance(self):
        return f"The number of times I dance is {self.dance}"


class Grandson(Son):
    dance = 4

    def is_dance(self):
        return f"I like to dance the most amazingest because i am the youngest! I dance {self.dance} times a week"


hussein = Dad()
sabi = Son()
jy = Grandson()


print(sabi.is_dance())
print(jy.is_dance())
#python looks for variables clsas by class --> top level down to the base class to see any overwrites.
print(jy.job)