# 03.	Write a Python function that returns the factorial of a number.

def findFact(num):
    fact = 1
    for i in range(2,num+1):
        fact=fact*i
    return fact
num = int(input("Enter A Number : "))
print("Factorial : ",findFact(num))
