# 6. Write a function to check if a number is a perfect square.

def checkPerfectSquare(num):
    a = 1
    while(a*a<=num):
        if(a*a==num):
            return True
        a=a+1
    return False
num = int(input("Enter A Number : "))
if(checkPerfectSquare(num)):
    print("It's A Perfect Square Number!")
else:
    print("It's Not A Perfect Square Number!")
