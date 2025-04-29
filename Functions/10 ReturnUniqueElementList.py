# 50.	Write a Python function that accepts a list and returns a new list with unique elements.


def findUnique(list1):
    return list(set(list1))
list1 = [2,5,3,7,8,5,9,7,6,9]

print("List : ",list1)
print("Unique List : ",findUnique(list1))
