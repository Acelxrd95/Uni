d1 = int(input("Enter the first mark: "))
d2 = int(input("Enter the second mark: "))
d3 = int(input("Enter the third mark: "))

marks = []
if d1>50 or d1==50:
    marks.append(d1)
if d2>50 or d2==50:
    marks.append(d2)
if d3>50 or d3==50:
    marks.append(d3)
print(marks)