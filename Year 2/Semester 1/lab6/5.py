from Stack_ADT import Stack

vals = [13, 9, 5, 4, 12]
rplc = 2
stack = Stack()
for v in vals:
    stack.push(v)

stack.replace(rplc)
print(stack)
