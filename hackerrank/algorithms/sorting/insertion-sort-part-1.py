#!/bin/python

def printar(ar, ret):
    ret = ret + str(ar[0])
    for i in range(1, len(ar)):
        ret = ret + " " + str(ar[i])
        
    return ret+"\n"

# Head ends here
def insertionSort(ar):    
    ret = ""
    tail = ar[len(ar)-1]
    i = len(ar) - 2

    while (i >= 0):
        if (ar[i] < tail):
            ar[i+1] = tail
            break
        else:
            ar[i+1] = ar[i]
            i = i - 1
        
        ret = printar(ar, ret)

    if (tail < ar[1]):
        ar[0] = tail

    ret = printar(ar, ret)     
    print ret

# Tail starts here
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)