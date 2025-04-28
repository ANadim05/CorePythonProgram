# 49. Write a function to convert a decimal number to binary.


def convertToBinary(num):
    binary = ""
    while(num>0):
        rem = num%2
        binary = str(rem)+binary
        num=int(num/2)
    return binary
num = int(input("Enter A Decimal Number : "))
print("Binary Number : ",convertToBinary(num))
