class Node:
    # Replace the next two lines with your code for (a)
    def __int__(self, value, next, prev):
      self.value = value
      self.next = next
      self.prev = prev 

class DoublyLinkedList:
    # Replace the next two lines with your code for (b)
    def __init__(self, head, tail):
      self.head = None

    def __str__(self):
        # Replace the next line with your code for (c)
        return "String output"

    def isEmpty(self):
        # Replace the next line with your code for (d)
        if head == None:
          return True
        return False

    def insertAtHead(self, item):
        # Replace the next line with your code for (e)
        if isEmpty(self) == True:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        else: self.head, item.next, item.prev, self.head.prev = item, self.head, None, item
        pass

    def insertAtTail(self, item):
        # Replace the next line with your code for (f)
        if self.tail == None:
          insertAtHead(self, item)
        else: self.tail, item.next, item.prev, self.tail.next = item, None, self.tail, item
        pass

          

    def popHead(self):
        # Replace the next line with your code for (g)
        x, self.head, self.head.next = self.head, self.head.next, None
        return x

    def popTail(self):
        # Replace the next line with your code for (h)
        
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


