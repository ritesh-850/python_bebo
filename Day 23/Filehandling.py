# Writing the data into text file
#open()
#one---path of file  second-------mode of file
#File is external resource
import os

file = open("C:/Users/rites/PycharmProjects/pythonProject/Day 23/FileHandling",'w')
file.write("This is my first instruction \n")
file.write("This is my second instruction \n")
file.write("This is my third instruction \n")
file.close()
print("Program Completed")

#Reading data from text file
file = open("C:/Users/rites/PycharmProjects/pythonProject/Day 23/FileHandling", 'r')
print(file.read())  # print all lines from console
print(file.readline()) #read first line from code
print(file.readable())
file.close()


#appending data into text file
file = open(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\FileHandling", 'a')
file.write("This is my fourth instruction \n")
file.write("This is my fifth instruction \n")
file.close()
print("Completed execution")

#Remove the file
try:
    os.remove(r"C:\Users\rites\PycharmProjects\pythonProject\Day 23\FileHandling")
    print("The file is deleted")
except FileNotFoundError as e:
    print(e)

#Remove the directory
os.rmdir(r"C:\Users\rites\PycharmProjects\pythonProject\ggdgd")
print("Directory is removed")