# 48. Write a function to check if a number is a palindrome.
# HINT:-  if you reverse a number so, if new number is exactly matched 
# with old one is Palindrome.


def findReverse(num):
    rev = 0
    while(num>0):
        rem = num%10
        rev = rev*10+rem
        num=int(num/10)
    return rev
num = int(input("Enter A Number : "))
if(num==findReverse(num)):
    print("Number is Palindrome!")
else:
    print("Number is Not Palindrome!")
