#binary search iterative

#use the floor library to make sure the index is an integer
from math import floor

# Insert your array here
A = [1,2,3,4,7,9,12,14,18]
# term to be searched
term = int(input("please enter a number:"))
n=len(A)    #get the length of the array
start=0    #set start to 0
end=n-1  # len(array) returns the size so we want the end index to be the true value
flag=False   #set flag to false
while (start<=end and flag==False):
	mid=floor((start+end)/2)
	if (A[mid]==term):
           flag=True
	elif (A[mid]>term):
		end=mid-1
	else:
		start=mid+1

if flag==True:
    print("term is found at position")
    print(mid)
else:
    print("Search term not found")
