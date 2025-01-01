import random
from problems import *
from sortingAlgorithms import *
from dataStructures import *
from searchAlgorithms import *

numbers = []

for i in range(100):
    numbers.append(random.randint(0,1))


#print(radixSort(numbers))
#print(binarySearch(numbers, 49, sorted=False))

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

l = Queue()
l.enqueue(n1)
l.enqueue(n2)
l.enqueue(n3)

print(l)
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
print(l)