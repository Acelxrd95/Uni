from random import randint
toss = []
t = input("Enter how many times do you want to roll the dice: ")
for i in range(0,int(t)):
    random_toss = randint(1,6)
    toss.append(random_toss)
print("Rolled: ",toss)
