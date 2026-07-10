#Python Program to Check if a String is Palindrome or Not

s = input()
if s == s[::-1]:
    print("Yes")
else:
    print("No")