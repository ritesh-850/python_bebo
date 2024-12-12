a = input("Enter the alphabet:")
b = input("enter the alphabet:")
if len(a)==len(b):
    if sorted(a)==sorted(b):
        print("anagram")
else:
        print("not anagram")
