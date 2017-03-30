class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self, newVal):
        n = Node(newVal)
        n.next = self.head;
        self.head = n;
        if (self.tail == None):
            self.tail = n

    def pop_front(self):
        if (self.head == None):
            return None

        n = self.head
        self.head = n.next;
        n.next = None
        
        if (self.head == None):
            self.tail = None

        return n

    def push_back(self, newVal):
        n = Node(newVal)
        if (self.tail == None):
            self.head = n
            self.tail = n
        else:
            self.tail.next = n;
            self.tail = n

    def pop_back(self):
        if (self.tail == None):
            return None

        if (self.tail == self.head):
            self.tail = self.head = None
            return None

        n = self.head
        while (n.next != self.tail):
            n = n.next
        
        n.next = None
        self.tail = n

    def printList(self):
        n = self.head
        while (n != None):
            print(n.data)
            n = n.next;

    def size(self):
        nrelem = 0
        n = self.head
        while (n != None):
            nrelem += 1
            n = n.next

        return nrelem

    def reverse(self):
        prev = None
        next = None
        current = self.head
        self.tail = current

        while (current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(next):
        self.next = next;


list1 = LinkedList()
list1.push_back(1)
list1.push_back(2)
list1.push_back(3)
list1.push_back(4)
list1.push_back(5)


list1.printList()

list1.reverse()
print("After Reversing")
list1.printList()

list1.push_back(9);
print("After Reversing")
list1.printList()
