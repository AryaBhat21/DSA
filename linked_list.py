class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def traversal(self):
        temp  = self.head
        while temp != None:
            print(temp.data, end = " ")
            temp = temp.next
        print("None")

    def add_at_begin(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def add_at_end(self,data):
        new1 = Node(data)
        temp = self.head
        #this loop goes to second last node to check if the next i.e the last node is None or not
        while temp.next != None:
            temp = temp.next
        temp.next = new1

    def del_at_begin(self):
        temp = self.head
        self.head = temp.next
    
    def del_at_end(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
    

#creating a node
n1 = Node(10)
sll = SLL()
#always head points at first node
sll.head = n1

n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3

sll.traversal()
sll.add_at_begin(5)
sll.traversal()

sll.add_at_end(40)
sll.traversal()

sll.del_at_begin()
sll.traversal()

sll.del_at_end()
sll.traversal()


