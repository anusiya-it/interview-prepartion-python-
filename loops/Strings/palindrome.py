a = int(input("enter a number:"))
original = a
rev = 0
while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10

if original == a:
    print ("palindrome")
else:
    print(" not palindrome")

