from Stack_ADT import Stack

string = "Coventry"
x = Stack()
for char in string:
    x.push(char)

print(x)
retstr = ""
for i in range(len(x)):
    retstr += x.pop()
print(retstr)
