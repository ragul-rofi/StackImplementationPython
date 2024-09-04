from prompt_toolkit.shortcuts import clear

stack = []
def push():
    m  = int(input())
    stack.append(m)
    print(stack)

def pop():
    e = stack.pop()
    print(e)
    print(stack)

def peek():
    print(stack[-1])

n = int(input("Enter size: "))
while True:
    c = int(input("Enter choice: "))
    if c== 1:
        push()
    elif c == 2:
        pop()
    elif c== 3:
        peek()
    elif c == 4:
        print("Exit")
        break
    else:
        print("Invalid Input")