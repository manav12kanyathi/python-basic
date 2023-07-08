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



class A:
    def num(self):
        x = 5
        y = 5
class B(A):
    def num1(self,x,y):
        z = x + y
        return z
obj = B()
obj.num()
obj.num1()
# print(v)







