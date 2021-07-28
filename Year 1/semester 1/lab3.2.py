A = [1,2,3,4,7,9,12,14,18]

max_n = A[0] 

min_n = 0
for i in A:
    if max_n > i:
        max_n = i
        
    if min_n < i:
        min_n = i
        
print(max_n)

print(min_n)