#Error : Syntax error, Logical Error, Runtime Error
#syntax error : wrong syntax of language---shown by compiler ----- eg: indentation error
#Logical error: expected output is not equal to actual output
#runtime error : Occurs at the execution of code----------dynamic binding---slower execution speed- more memory usage
#Compiletime error : higher execution speed - less memory usage

#log :
print("start")
try:
    print(10/5)
    print(list[5])
except Exception as a:
    print(a)
print("end")


# log :
num1 , num2 = 10,5
try:
    result = num1/num2
    print(result)
# except ZeroDivisionError:
#     print("thrown Zero division error")
# except FileNotFoundError:
#     print("File not found exception")
except SyntaxError as e:
    print(e)
# except Exception as e:
#     print(e)
else:
    print("No exception occurred")
finally:
    print('always Executed')

# Raising our own exception
def Enter(num):
    if num < 0:
        raise ValueError()
    if num % 2== 0:
        print("even")
    else:
        print("odd")
num = 5
try:
    Enter(num)
except ValueError:
    print("This is exception in code")
print("program terminated")


