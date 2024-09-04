class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next=self.head
            self.head=newnode

    def pop(self):
        self.head = self.head.next

    def peek(self):
        print(self.head.data)

    def display(self):
        temp = self.head
        while(temp!= None):
            print(temp.data,id(temp.next))
            temp = temp.next

obj = stack()
n = int(input("Enter size: "))
for i in range(n):
    m = int(input("Enter Element: "))
    obj.push(m)
obj.display()
obj.pop()
obj.display()
obj.peek()
obj.display()












