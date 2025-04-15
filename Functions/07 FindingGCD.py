# 07. Write a function that returns the greatest common divisor (GCD) of two numbers.



def findGCD(num1,num2):
    a = 1
    gcd = a
    while(a<=num1):
        if( num1%a==0 and num2%a==0 ):
            gcd=a
        a=a+1
    return gcd
num1 = int(input("Enter A Number : "))
num2 = int(input("Enter B Number : "))
print("GCD : ",findGCD(num1,num2))
