 # single inheritance



# class A:
#     def add(self):
#         print('this is addition')
#     def sub(self):
#         print('this is subtract')
# class B(A):
#     def mul(self):
#         print('this is multiply')
    
# obj = B()
# obj.add()
# obj.mul()
# obj.sub()


# class A:
#     def person(self):
#         name = "manav"
#         age = 25
#         occupation = "student"
#         return name, age, occupation 
# class B(A):
#     def person1(self):
#         name = "manav kanyathi"
#         age = 20
#         occupation = "student"
#         # return name, age
# obj = B()
# print(obj.person()[1])
# # obj.person1()






# class A:
#     name = "manav"
#     age = 25
#     occupation = "student"
#     # def person(self):
#     #     name = "manav"
#     #     age = 25
#     #     occupation = "student"
#     #     return name
# # # class B(A):
# # #     def person1(self):
# # #         name = "manav kanyathi"
# # #         age = 20
# # #         occupation = "student"
# obj = A()
# # obj.person()
# # obj.person1()

# print(obj.name,obj.age)




# class A:
#     def num(self):
#         for i in range(3):
#             # username = "manav"
#             username = input('enter username')
            
#             if username == "manav":
#                     print('Device is ready')
#                     break
#             else:
#                     print('Device is not ready')
#         for x in range(3):
#         # password = "manav123"
#             password = input('enter password')
        
        
                
#             if password == "manav123":
#                     print('password matched')
#                     break
#             else:
#                     print('password does not matched')

      
# class B(A):

#     def num1(self):
       
#       print('Done')
   
# obj = B()
# obj.num()
# obj.num1()




# class A:
#     def num(self):
#         x = 10
#         y = 10
#         z = x + y
#         return z
# class B(A):
#     def num1(self):
#         print('Addtion')
# obj = B()
# obj.num1()
# v = obj.num()
# print(v)




# class A:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll
#     # name = 'helo'
#     # roll = 132

#     def price(self):
#         print(self.name,self.roll)
    
#     def helo(self):
#         print(self.name,self.roll)

# name = input('enter username')
# roll = input('enter roll no')
# obj = A(name,roll)
# obj.helo()



# class A:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def num(self):
#         print(self.x,self.y)
#         z = self.x + self.y
#         return z
# obj = A(5,5)
# v = obj.num()
# print(v)



class A:
    def __init__(self,fees):
        # self.collegename = collegename
        # self.name = name
        # self.course = course
        # self.age = age
        self.fees = fees

    def school(self):
        self.collegename = 'DAV college'
        print(self.collegename)
    def student1(self):
        self.name = 'manav'
        self.course = 'bca'
        self.age = 23
        print(self.name,self.course,self.age,self.fees)
    def student2(self):
       self.name = 'rahul'
       self.course = 'mca'
       self.age = 24
       print(self.name,self.course,self.age,self.fees)
    def student3(self):
       self.name = 'aman'
       self.course = 'mba'
       self.age = 25
       print(self.name,self.course,self.age,self.fees)

class B(A):
    def student4(self):
        self.name = 'aniket'
        self.course = 'dca'
        self.age = 26
        print(self.name,self.course,self.age,self.fees)
# collegename = 'DAV college'
obj = B(20000)
obj.school()
obj.student1()
obj.student2()
obj.student3()
obj.student4()




