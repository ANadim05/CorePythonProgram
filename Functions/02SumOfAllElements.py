# write a python program to calculate the sum of all the element in the list.

def sumlist(li):
    total=0                                                    #initial value of total
    for i in li:
        total=total+i                                          # Add i in total 
    return(total)

print("sum of list:", sumlist([10,1,2,3,4]))                   #sum of list: 20
