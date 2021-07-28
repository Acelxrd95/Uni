import time

name  = input("please enter your name:")
print(f'Hello, {name}')

word = ['a','p','p','l','e']
word_q = []
for i in range(0,len(word)):
    word_q.append("_")

print(f"the word consists of {len(word)} letters can you guess the word?")
print(*word_q)

    
for i in range(0,10):
    print(f'---------------------------------------\nTrial {i+1} of 10')
    t1 = str(input("enter letter: "))

    for ii in range(0,len(word)):
        if t1 == word_q[ii]:
            print(f"you already used the letter {t1}\n---------------------------------------")
        elif t1 == word[ii]:
            word_q[ii] = t1
    if word_q == word:
        print('you guessed the word "', *word, '"')
        break
    elif i == 9:
        print("---------------------------------------\nyou lost")
    else:
        print(*word_q)
