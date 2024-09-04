class Stack:
    def __init__(self,val):
        self.val = val
        self.top = -1
        self.arr = [None]*val

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.val-1

    def push(self,elem):
        if self.is_full():
            print("Over flow")
            return
        else:
            self.top += 1
            self.arr[self.top] = elem

    def pop(self):
        if self.is_empty():
            print("Under Flow")
            return None
        else:
           elem = self.arr[self.top]
           self.top -=1
           return elem

    def peek(self):
        return self.arr[self.top]

n = int(input("Enter size: "))
Stack = Stack(n)
while True:
    c = int(input("Enter Choice: "))
    if c == 1:
        elem = int(input("Enter element: "))
        Stack.push(elem)

    elif c == 2:
        res = Stack.pop()
        print("Element removed: ",res)

    elif c == 3:
        res = Stack.peek()
        print("Element on top: ",res)

    elif c == 4:
        print("Exited")
        break
    else:
        print("Invalid Input")






















