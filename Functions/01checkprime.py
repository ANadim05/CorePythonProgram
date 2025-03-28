"""Write a python function to check if a number is prime or not"""

# A prime number has only two factors.

def checkprime(num):
    count=0                                         #initial value of count is 0
    
    for i in range(1,num+1):
        if (num%i==0):                                      
            count=count+1                           # when you got factor then add 1 in count
    if (count==2):
        return "prime"
    else:
        return "Not Prime"

print(checkprime(24))                             #Not Prime
print(checkprime(19))                             #prime
