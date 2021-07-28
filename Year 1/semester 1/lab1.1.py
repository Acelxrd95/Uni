import random

u1 = random.randint(65,90)
u2 = random.randint(65,90)
l1 = random.randint(97,122)
l2 = random.randint(97,122)
d1 = random.randint(48,57)
d2 = random.randint(48,57)
sc1 = random.randint(33,47)
sc2 = random.randint(33,47)

pass_unf = [chr(u1),chr(u2),chr(l1),chr(l2),chr(d1),chr(d2),chr(sc1),chr(sc2)]
random.shuffle(pass_unf)

for i in range(0,8):
    print(pass_unf[i])