from Stack_ADT import Stack

stack = Stack()
values = [12, 4, 5, 9, 13, 6]
even = 0
odd = 0

for v in values:
    stack.push(v)

for e in stack:
    if e % 2 == 0:
        even += 1
    else:
        odd += 1

print(even == odd)
