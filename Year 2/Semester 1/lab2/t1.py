lists = [1,1,2,3,4,5,1,2]
list2=[]
x = int(input("number to check against: "))
for item in lists:
    if x != item:
        list2.append(item)

print(list2)