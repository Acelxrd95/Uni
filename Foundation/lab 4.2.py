marks = []
for i in range(1,4):
    if i == 1:
        x = "first degree"
    elif i == 2:
        x = "second degree"
    elif i == 3:
        x = "third degree"
    d = input(f"Enter the {x}: ")
    if int(d)>=50:
        marks.append(d)
print(marks)