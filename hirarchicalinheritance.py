class A:
    def func1(self):
        print('this is parent class')
class B(A):
    def func2(self):
        print('this is first child class')
class C(A):
    def func3(self):
        print('this is second child class')
obj1 = B()
obj2 = C()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()