# class A:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll

#     def func1(self):
#         print('the name is :', self.name,'and the roll no is : ',self.roll)

# obj = A('heloname',123123)
# obj.func1()

# v = '77777'
# c = 'poopopop'
# print('the name is :',v , 'the roll is',c)




class A:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def func(self):
        print('my fname is :',self.fname,'and lname is :',self.lname,'and age is :',self.age)
obj = A('manav','kanyathi',25)
obj.func()