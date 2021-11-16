from Stack_ADT import Stack

stack = Stack()
otrstr = ""
string = "(([)])"
for char in string:
    if char == "(" or char == "{" or char == "[":
        stack.push(char)
    else:
        otrstr += char

for char in otrstr:
    if stack.isEmpty and char != None:
        print("Unbalanced string")
    if stack.peek() == "(" and char == ")":
        stack.pop()
    elif stack.peek() == "{" and char == "}":
        stack.pop()
    elif stack.peek() == "[" and char == "}":
        stack.pop()

if not stack.isEmpty():
    print("Unbalanced string")
else:
    print("Balanced string")
