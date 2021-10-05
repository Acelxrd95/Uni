testlist = ['G',"F","G",'I',"S",'B','E','S','T']
repr_char = "*"
ret_char = input("Enter a character to exclude: ")

for i in range(len(testlist)):
    if testlist[i] != ret_char:
        testlist[i] = repr_char
print(testlist)