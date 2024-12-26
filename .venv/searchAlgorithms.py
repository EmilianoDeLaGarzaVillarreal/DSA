from sortingAlgorithms import bucketSort, radixSort


def binarySearch(arr, val, hi = 0, lo = 0, sorted=False):
    hi = len(arr)
    while lo < hi: #condition to stop while loop, when high and low cross it stops
        midpoint = lo+(hi-lo)//2 #updating midpoint
        if sorted: #does not sort
            if val == arr[midpoint]:
                return midpoint #returned if midpoint == value
            elif val < arr[midpoint]:
                hi = midpoint #updates high if midpoint < val
            elif val > arr[midpoint]:
                lo = midpoint + 1 #updated low while getting rid of mid point
        else: #sorts array
            arr = radixSort(arr)
            sorted = True #same as above
            if val == arr[midpoint]:
                return midpoint
            elif val < arr[midpoint]:
                hi = midpoint - 1
            elif val > arr[midpoint]:
                lo = midpoint + 1
    return -1