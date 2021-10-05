shift=int(input("Enter shift value: "))
test_list = ["C",'o','v','e','n','t','r','y']
for i in range(len(test_list)):
    currord = ord(test_list[i])
    if currord >= 90-shift and currord<=91:
        currord-=26
    elif currord >= 122-shift:
        currord-=26
    test_list[i]=chr(currord+shift)
print(test_list)