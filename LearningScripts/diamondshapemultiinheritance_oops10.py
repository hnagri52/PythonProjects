class A:
    def met(self):
        print("I am inside class A")


class B(A):
    def met(self):
        print("I am inside class B")
class C(A):
    def met(self):
        print("I am inside class C")

class D(B,C):
    def met(self):
        print("I am inside class D")

a = A()
b = B()
c = C()
d = D()

#python address the diamond shape problem with multiple inheritance

a.met()
b.met()
c.met()
d.met()