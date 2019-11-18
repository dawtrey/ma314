class Node:
    # Replace the next two lines with your code for (a)
    def __init__(self, value, next, prev):
      self.value = value
      self.next = next
      self.prev = prev 

class DoublyLinkedList:
    # Replace the next two lines with your code for (b)
    def __init__(self):
      self.head = None
      self.tail = None

    def __str__(self):
        # Replace the next line with your code for (c)
        if self.head == None:
            a = "Empty"
        else:   
            a = str(self.head.value)
            b = self.head
            while b.next != None:
                a += " <-> " + str(b.next.value)
                b = b.next
        return "List: " + a

    def isEmpty(self):
        # Replace the next line with your code for (d)
        if self.head == None:
          return True
        return False

    def insertAtHead(self, item):
        # Replace the next line with your code for (e)
        x = Node(item, None, None)
        if self.tail == None:
            self.head = x
            self.tail = x
        else: self.head, x.next, x.prev, self.head.prev = x, self.head, None, x 
        pass

    def insertAtTail(self, item):
        # Replace the next line with your code for (f)
        x = Node(item, None, None)
        if self.tail == None:
          insertAtHead(self, item)
        else: 
            self.tail.next =  x
            self.tail, x.next, x.prev = x, None, self.tail 
        pass
          

    def popHead(self):
        # Replace the next line with your code for (g)
        if DoublyLinkedList.isEmpty(self):
            return "None" 
        x = self.head.value
        if self.head == self.tail:
            self.head, self.tail = None, None
            return x
        self.head = self.head.next
        return x

    def popTail(self):
        # Replace the next line with your code for (h)
        if DoublyLinkedList.isEmpty(self):
            return "None" 
        x = self.tail.value
        if self.head == self.tail:
            self.head, self.tail = None, None
            return x
        
        self.tail = self.tail.prev
        self.tail.next = None
        return x

if __name__ == '__main__':
    A = DoublyLinkedList()
    A.insertAtHead(6)
    print(A)
    A.insertAtHead(7)
    print(A)
    A.insertAtTail(3)
    print(A)
    A.insertAtTail(4)
    print(A)
    print(A.popHead())
    print(A)
    print(A.popTail())
    print(A)
    print(A.popTail())
    print(A)
    print(A.popTail())
    print(A)
    print(A.popTail())
    print(A)
# Output should be:
# List: 6
# List: 7 <-> 6
# List: 7 <-> 6 <-> 3
# List: 7 <-> 6 <-> 3 <-> 4
# 7
# List: 6 <-> 3 <-> 4
# 4
# List: 6 <-> 3
# 3
# List: 6
# 6
# List: Empty
# None
# List: Empty


