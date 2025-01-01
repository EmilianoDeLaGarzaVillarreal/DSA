class Node:
    prev = None
    next = None
    data = None

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

class DoubleLinkedList: #Double linked list implementation

    def __init__(self): #initiates with two variables, both pointing to None
        self.l = 0
        self.head = None
        self.tail = None

    def __str__(self): #method to conver DLL to string
        node = self.head
        out = ""
        while node.next: #runs as long as node is pointing to another node
            out += str(node) + " "
            node = node.next
        out += str(node) #added last node element in here to avoid extra string space
        return out

    def getLength(self): #returns length of DLL
        return self.l

    def getNode(self, ind): #Gets node based on index passed by user
        if ind >= self.l: #if index is over DLL length, it will throw an error while returning -1
            return 0
        node = self.head
        current = 0
        while current < ind: #runs for lenth of index
            node = node.next
            current += 1
        return node #returns node at said index

    def append(self, node): #appends new nodes to the DLL
        if self.l == 0: #in case DLL is empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node #make sure to update the links appropiately
            node.prev = self.tail
            self.tail = node
        self.l += 1 #increase length attribute of DLL

    def appendNodeList(self, nodeList): #uses append method to append list of nodes
        for node in nodeList:
            self.append(node)

    def remove(self, node): #removes node specified on method
        if node.next and node.prev: #if the node has both attributes it will update the links accordingly
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.next = node.prev = None
        elif node.next and not node.prev: #missing prev node means it is the head being removed
            nextNode = node.next
            self.head = nextNode #make sure to update the head in the DLL
            nextNode.prev = None
            node.next = None
        elif node.prev and not node.next: #tail being removed
            prevNode = node.prev
            self.tail = prevNode #make sure to update the tail in the DLL
            prevNode.next = None
            node.prev = None
        self.l -= 1 #reduce DLL length
        return node


    def insertAt(self, node, ind):
        if self.l == 0:
            self.append(node)
            return node
        myNode = self.getNode(ind)
        if not myNode: #Outside current length
            return 0
        if myNode.next and myNode.prev: #In between
            prevNode = myNode.prev
            nextNode = myNode.next
            prevNode.next = node
            myNode.prev = node
            node.next = myNode
        elif myNode.next and not myNode.prev: #this means we are inserting new head
            myNode.prev = node
            node.next = myNode
            self.head = node
        elif not myNode.next and myNode.prev: #before the tail
            prevNode = myNode.prev
            prevNode.next = node
            myNode.prev = node
            node.next = myNode
        self.l += 1
        return node

class LinkedList:

    def __init__(self):
        self.l = 0
        self.head = None
        self.tail = None

    def __str__(self):
        if self.l == 0:
            return " "
        node = self.head
        out = ""
        while node.next:
            out += str(node) + " "
            node = node.next
        out += str(node)
        return out

    def append(self, node):
        if self.l == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.l += 1

    def pop(self):
        node = self.tail
        prevNode = self.tail.prev
        self.tail = prevNode
        self.tail.next = None
        return node

    def dequeue(self): #method more specific to queue
        if self.l == 0:
            return 0
        node = self.head
        self.head = node.next
        node.next = None
        self.l -= 1
        return node

class Queue: #implemented from linked list as it basically a more specific linked list

    def __init__(self):
        self.list = LinkedList()

    def __str__(self):
        return self.list.__str__()

    def enqueue(self, node):
        self.list.append(node)

    def dequeue(self):
        return self.list.dequeue()

    def peek(self):
        return self.list.head
