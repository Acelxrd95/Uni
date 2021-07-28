def sum_avg(some_list):
    return sum(some_list). sum(some_list)/len(some_list)

def sum_avg_2(x,y,z):
    sum = x
    return sum,avg



marks = []
ii = ''
for i in range(1,4):
    if i == 1:
        ii = "first degree"
    elif i == 2:
        ii = "second degree"
    elif i == 3:
        ii = "third degree"
    d = input(f"Enter the  {ii}: ")
    marks.append(int(d))

sum_avg(marks)

print("The sum of marks is: ",sum(marks))
print("The average of marks is: ", sum(marks)/len(marks) )