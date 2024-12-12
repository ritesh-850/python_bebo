# #Task 1
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\log",'w')
# file.write("Python program is interesting into it")
# file.close()
# print("Completed")
#
# #Task 2
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\log",'r')
# print(file.read())
# file.close()
# import datetime
#
# #Task 3
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\log",'w')
# current_datetime = datetime.datetime.now()
# file.write(f"{current_datetime}")
# file.close()
# print("Completed")
from os import linesep

#Task 4
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\document", 'r')
# content = file.read()
# words = content.split()
# print(len(words))
#
# #Task 5
# file = open(r"C:\Users\rites\Desktop\bebo\Book1.csv")
# print(file.read())
# file.close()
#
# #Task 6
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\source",'r')
# read = file.read()
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\destination",'a')
# file.write(f"{content}")
# file.close()

#task 7
try:
    with open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\Mergedfile", "r") as file:
        lines = file.readlines()

    with open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\Mergedfile", "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        alphabet_count = 0
        for char in content:
            if char.isalpha():
                alphabet_count += 1
        line_count = len(lines)

        print(f"The number of words in 'document.txt' is: {word_count}")
        print(f"The number of alphabetic characters in 'document.txt' is: {alphabet_count}")
        print(f"The number of lines in 'document.txt' is: {line_count}")
except FileNotFoundError as e:
    print(e)









#Task 8
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\source",'r')
# read = file.read()
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\log",'r')
# read1 = file.read()
# file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\Mergedfile",'w')
# file.write(f"{read1}{read}")
# file.close()
# print("merge completed")



