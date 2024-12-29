import math
from sortingAlgorithms import *

def binarySearch(arr, val, hi = 0, lo = 0, sorted=False):
    hi = len(arr)
    if not sorted:
        arr = radixSort(arr)
        sorted == True
    while lo < hi: #condition to stop while loop, when high and low cross it stops
        midpoint = lo+(hi-lo)//2 #updating midpoint
        if val == arr[midpoint]:
            return midpoint #returned if midpoint == value
        elif val < arr[midpoint]:
            hi = midpoint #updates high if midpoint < val
        elif val > arr[midpoint]:
            lo = midpoint + 1 #updated low while getting rid of mid point
    return -1

def minIndSqrtJmp(arr, val, sorted=False):#Used to find min index O(sqrt(n))
    jmp = int(math.sqrt(len(arr))//1)
    ind = 0
    if not sorted:
        arr = radixSort(arr) #sorts
        sorted = True
    while ind < len(arr): #will exit when ind+=jmp passes len(arr)
        if arr[ind] == val: #if equal then linear search previous values
            for j in range(ind-jmp+1,ind+1): #not including previous jmp index but including current jmp index
                if arr[j] == val:
                    return j #return min index
        else:
            ind += jmp #changes on jmp quantity
    for j in range(ind-jmp+1,-1): #to do last slice of array, in case it jumps over
        if arr[j] == val:
            return j
    return -1 #if not there then -1




