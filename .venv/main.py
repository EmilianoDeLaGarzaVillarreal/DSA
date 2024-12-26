import random
from sortingAlgorithms import *
from dataStructures import *
from searchAlgorithms import *

numbers = []

for i in range(100):
    numbers.append(random.randint(1,100))


print(radixSort(numbers))
print(binarySearch(numbers, 99, sorted=False))
