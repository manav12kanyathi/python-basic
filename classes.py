# class name:

#     def add(self):
#         print('this is classes')
# obj  = name()
# obj.add()




# class myclass():

#     def name(self):
#         print('This is my class')
# a = myclass()
# a.name()


# class myclass():
#     def num(self):
#         num1 = int(input('enter a no'))
#         num1 = num1 + 1
#         print('addition',num1)
# x = myclass()
# x.num()



# class myclass():
#     # num = int(input('enter a number'))
#     def add(self):
#         x = int(input('enter a number'))
#         y = int(input('enter a number'))
#         print('addition',x+y)
#     def sub(self):
#         x = int(input('enter a number'))
#         y = int(input('enter a number'))
#         print('subtract',x-y)
# x = myclass()
# i = int(input('enter a no'))
# if i == 1:
   
#     x.add()
# elif i == 2:

#     x.sub()
# else:
#     print('invalid input')






# class myclass():
#     def num(self):
#         for i in range(3):
#             username = input('enter user name')
#             if username == 'manav':
#                 break
#             else:
#                 print('Re enter the user name')
#         else:
#             print('Try again later')

#         for x in range(3):
#             password = input('enter a password')
#             if password == 'manav123':
#                 print('Login Successful')
#                 break
#             else:
#                 print('Try Again')
#         else:
#             print('invalid password')
# a = myclass()
# a.num()






# import time       
# class myclass():
#     def num(self):
#             pin = int(input('enter pin'))    
#             if pin == 1810:
#                 print('Device is ready')  
#             else:
#                     pin = int(input('enter pin'))
#                     for i in range(3):
#                         print(i)
#                         def countdown(time_sec):
#                                 while time_sec:
#                                     mins, secs = divmod(time_sec, 60)
#                                     timeformat = '{:02d}:{:02d}'.format(mins,secs)
#                                     print(timeformat,end='\r')
#                                     time.sleep(1)
#                                     time_sec -= 1
#                         countdown(30)
# a = myclass()1810
# a.num()

# def countdown(time_sec):
#             # print('conuntdown calls')
#             while time_sec:
#                 mins, secs = divmod(time_sec, 60)
#                 timeformat = '{:02d}:{:02d}'.format(mins,secs)
#                 print(timeformat,end='\r')
#                 time.sleep(1)
#                 time_sec -= 1


# import time

# # pin = 0
# class myclass():
#     def num(self):
#         attempt = 0
#         for i in range(1,4):
#             pin = int(input("please enter your password"))
#             if pin == 1810:
#                 print('password is correct')
#                 break
#             else:
#                 print('wrong password')
#                 # print(i)
#                 if i == 3:
#                     countdown(5)
#                     # attempt = attempt+1
#                     # if attempt == 1:
#                     for i in range(1,4):
#                         pin = int(input("please enter your password"))
#                         if pin == 1810:
#                             print('password is correct')
#                             break
#                         else:
#                             if i == 3:
#                                 # print('pls  wait for 60 sec')
#                                 countdown(7)
# obj = myclass()
# obj.num()







                        






#  while loop



class myclass():
    def num(self):
        attempt = 0
        while attempt != 3:
            pin = int(input('enter pin'))
            if pin == 1810:
                print('Device is ready ')
                break
            elif pin != 1810:
                        attempt = attempt + 1
                        if attempt == 3:
                            def countdown(time_sec):
                                    while time_sec:
                                        mins, secs = divmod(time_sec, 60*2)
                                        timeformat = '{:02d}:{:02d}'.format(mins,secs)
                                        print(timeformat,end='\r')
                                        time.sleep(1)
                                        time_sec -= 1
                                        # print("Timer Ended")
                            countdown(30)
a = myclass()
a.num()

