# 04.	Write a Python function to find the maximum of three numbers.



def findLargest(tuple1):
    return max(tuple1)


num1 = int( input("Enter A Number : ") )
num2 = int( input("Enter B Number : ") )
num3 = int( input("Enter C Number : ") )


print("Largest Value : ",findLargest((num1,num2,num3)))
