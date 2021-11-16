from Stack_ADT import Stack

stack = Stack()
# {0, 1, 2, 3, 4, 5, 6, 7, 8,9, +, -, *, / }
oprand = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
operator = ["+", "-", '*', "/"]
string = "234+*"
for char in string:
    if char in oprand:
        stack.push(char)
    if char in operator:
        x = int(stack.pop())
        y = int(stack.pop())
        z = 0
        if char == "+":
            z = x + y
        elif char == "-":
            z = x - y
        elif char == "*":
            z = x * y
        elif char == "/":
            z = x / y
        stack.push(z)

print(stack.pop())