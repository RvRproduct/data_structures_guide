"""
Roberto Reynoso
Stacks Solution
"""

from collections import deque

# Stacks (LIFO) order
class MyStacks():
    
    def __init__(self):
        self.stack = deque()

# push to the stack
    def push_stack(self):
        item = input("Add an item to the stack: ")
        self.stack.append(item)

# remove from the stack
    def remove_stack(self):
        if self.stack:
            self.stack.pop()
        else:
            print(f"The stack is empty: {self.stack}")

# user menu
    def menu(self):
        select = ""
        while True:
            select = input("""1. Push
2. Remove
3. Return Stack
Choice: """)
            if select == "1":
                MyStacks.push_stack(self)
            elif select == "2":
                MyStacks.remove_stack(self)
            elif select == "3":
                break
        print(f"Stack: {self.stack}")


start_stack = MyStacks()
start_stack.menu()
