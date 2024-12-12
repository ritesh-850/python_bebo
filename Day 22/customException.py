#Created by user itself
# class MyException(Exception):
#     pass
# try:
#     raise MyException("This is a custom error message")
# except MyException as e:
#     print(e)

#
class NegativeNumberError(Exception):
    def __init__(self,msg="Negative values are not allowed"):
        self.msg = msg
        super().__init__(self.msg)
def check(num):
        if num < 0:
            raise NegativeNumberError("Please provide positive number")
        else:
            print(f"the number {num} is positive")
try:
    num = int(input("Enter the number:"))
    check(num)
except NegativeNumberError as e:
    print(e)
except ValueError as a:
    print(a)
except Exception as b:
    print(b)