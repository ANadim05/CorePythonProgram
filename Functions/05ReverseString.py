# 05.	Write a Python function to reverse a string.


def reverseString(str1):
    revStr = ""
    
    for i in range(len(str1),0,-1):
        revStr = revStr+str1[i-1]
    return revStr

str1 = input("Enter A String : ")
print("Reverse String : ",reverseString(str1))
