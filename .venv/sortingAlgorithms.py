def mergeSort(arr):#O(n*log(n))
    arrLen = len(arr)
    arrOne = []
    arrTwo = []
    for i in range(int(arrLen/2)): # divides array into two arrays
        arrOne.append(arr[i])
    for i in range(arrLen-1, int(arrLen/2-1), -1):
        arrTwo.append(arr[i])

    if len(arr) == 1: #base condition to end recursion
        return arr

    arrOne = mergeSort(arrOne) #recursion on left side
    arrTwo = mergeSort(arrTwo) #recursion of right side

    finalArr = [] #creation for final result and join the two above arrays
    i, j = 0, 0
    while len(arrOne) > i and len(arrTwo) > j: #checks if any of the two arrays has given all its elements
        if arrOne[i] < arrTwo[j]: #decides if we first give left of right array element
            finalArr.append(arrOne[i])
            i += 1
        else:
            finalArr.append(arrTwo[j])
            j += 1

    if len(arrOne) > i: #leftover elements
        for z in range(len(arrOne) - i):
            finalArr.append(arrOne[i])
            i += 1

    if len(arrTwo) > j:
        for z in range(len(arrTwo) - j):
            finalArr.append(arrTwo[j])
            j += 1

    return finalArr

def bubbleSort(arr):#O(n^2)
    ordered = True
    for i in range(len(arr)): #we need to go through the entire array
        for j in range(len(arr) - i - 1): #like bubbles, but in this case bigger values float first each iteration
            if arr[j] > arr[j+1]:           # of j one space to the right.
                old = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = old            #updates to swap bigger to the right
                ordered = False         # if we entered the if statement once during the loop then the array is not ordered yet
        if ordered:
            return arr
    return arr

def insertionSort(arr): #O(n^2)
    for i in range(1, len(arr)):
        current = arr[i]
        index = i
        while current < arr[index-1]:
            if index == 0:
                break
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = current
    return arr

def selectionSort(arr):#O(n^2)
    for i in range(len(arr)):
        minInd = i
        for j in range(i + 1, len(arr)):
            if arr[minInd] > arr[j]:
                minInd = j
        temp = arr[i]
        arr[i] = arr[minInd]
        arr[minInd] = temp
    return arr

def quickSort(arr):
    left = 0
    right = len(arr) - 1
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        if arr[left] <= arr[right]:
            left += 1
            continue
        if arr[i] <= arr[right]:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    leftArr = quickSort(arr[0:left])
    rightArr = quickSort(arr[left:right+1])

    return leftArr + rightArr

def countingSort(arr): #O(n+max)
    biggest = arr[0]
    for i in arr:
        if i > biggest:
            biggest = i
    d = dict(zip(range(biggest+1), [0]*(biggest+1)))
    for i in arr:
        d[i] += 1
    arr = []
    for k in d:
        for v in range(d.get(k)):
            arr.append(k)

    return arr

def radixSort(arr):#O(n+k)
    biggest = arr[0]
    maxSize = 1
    size = 10
    for i in arr:
        if i > biggest:
            biggest = i
    while biggest % (maxSize) != biggest:
        maxSize *= 10
    d = dict()
    run = 0
    while size < maxSize+1:
        for i in range(10):
            d[i] = []
        for i in range(len(arr)):
            d[(arr[i] % size) // (10**run)].append(arr[i])
        arr = []
        for k in d:
            for v in d.get(k):
                arr.append(v)
        size *= 10
        run += 1
    return arr

def bucketSort(arr):#Used for floating point values...
    #bucket creation
    big = arr[0]
    for i in arr:
        if i > big:
            big = i
    d = dict()
    for i in range(10):
        d[(big//10+1)*(i+1)] = []
    #bucket assigning
    for item in arr:
        for k in d:
            if item<=k:
                d[k].append(item)
                break
    arr = []
    for k in d:
        for i in quickSort(d[k]):
            arr.append(i)
    return arr


