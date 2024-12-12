#static method calling without creating object
#static method creation
class myclass:
    def m1(self):
        print("This is instance method")
    @staticmethod
    def m2(num):
        print(num)
obj = myclass()
obj.m1()
obj.m2(10)


#variables in python
# class myclass:
#     a,b=10,20
#     def add(self):
#         print(self.a + self.b)
#     def mul(self):
#         print(self.a * self.b)
#
# mc = myclass()
# mc.add()
# mc.mul()

#
# i, j = 15,25
# class myclass:
#     a,b=10,20
#     def add(self,x,y):
#         print(x,y)
#         print(self.a + self.b)
#         print(i,j)
#
# mc = myclass()
# mc.add(10,20)

#using same name for all variables
# i,j=10,20
# class MyClass:
#     i,j=10,20
#     def add(self,i,j):
#         print(i,j)       #print local variable
#         print(self.i + self.j)     #print instance variable
#         print(globals()['i'],globals()['j'])         #print global variable
#
# mc = MyClass()
# mc.add(3,4)