# sentence = input("Enter the sentence:")
# words_split = sentence.split()
# for i in words_split:
#     print(i[-1::-1],end=" ")

#replace the word
# word = (input("Enter the word:"))
# replace_word = ""
# for i in word:
#     if i == "a":
#         replace_word +="o"
#     else:
#         replace_word += i
# print(replace_word)
# print()

#occurance
# word=input("Enter the number:")
# occur={}
# for i in word:
#     if i in occur:
#         occur[i]+=1
#     else:
#         occur[i]=1
# print(occur)

# longest word from string
sentence = input("Enter the sentence:")
words = sentence.split()
long = ""
for i in words:
    if len(i) > len(long):
        long=i
print(len(long))


# find the first non repeating element













