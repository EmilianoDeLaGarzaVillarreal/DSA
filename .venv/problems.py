from searchAlgorithms import *


def crystalBalls(arr):
    minFloor = minIndSqrtJmp(arr, 1) #calls for O(sqrt(N)) function to find min ind for crystal ball to break
    return minFloor #returns index