def sub_two(x,y):
    z = x - y
    z2 = x + y
    return z,z2

# ================================================================================

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(sub_two(n1,n2))
