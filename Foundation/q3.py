from random import randint

def dice_throwing(x):   #throwing of dice
    throw_1 = randint(1,6)
    throw_2 = randint(1,6)
    sums = throw_1 + throw_2
    return(throw_1,throw_2,sums)

def frequency(mylist):              #calculation of the frequency of sums
    temp_list = [[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0]]
    return_list = []
    for x in range (0,len(mylist)):
        for i in range (0, 11):
          if mylist[x] ==  temp_list[i][0]:
              temp_list[i][1] += 1
    for i in range (0,11):
        if temp_list[i][1] > 0:
            return_list.append(temp_list[i])
    return(return_list)

def mode(mylist):                  #calculation of mode
    temp = []
    tempno = mylist[0][1]
    tempindex = 0

    for i in range (1,len(mylist)):
        if mylist[i][1] > tempno:
            tempno = mylist[i][1]
            tempindex = i

    for i in range (1,len(mylist)):
        if mylist[i][0] != mylist[tempindex][0]: 
            if mylist[i][1] == tempno:
                temp.append(mylist[tempindex])
    temp.append(mylist[tempindex])
    return(temp)

# =========================================================================================================================

trials_and_sums = []
file = open('results.txt','w')
file.write("========TRIALS AND THEIR SUMS: ========\nTrial No:\tTrial:\t\tSum:\n=======================================")
freq_t = []
freq_sum = 0

for i in range (0,1000):                     #rolling of dice 1000 times
    trials_and_sums.append(dice_throwing(0))
    freq_t.append(trials_and_sums[i][2])
    file.write(f"\n{str(i+1)}\t\t({trials_and_sums[i][0]},{trials_and_sums[i][1]})\t\t {trials_and_sums[i][2]}")
    freq_sum += trials_and_sums[i][2]

file.write("\n===========FREQUENCY TABLE: ===========\n=======================================\nNumber:\t\tFrequency:")

freq_t.sort()
freq_res = []
freq_res = frequency(freq_t)

for i in range (0,11):
    file.write(f"\n{freq_res[i][0]}\t\t\t{freq_res[i][1]}")

mean = freq_sum/1000

stat_mode = mode(freq_res)

file.write('\n=============STATISTICS: ==============\n=======================================\nMean:\tMedian:\t\tMode:\t Mode Count:')
file.write(f"\n{mean}\t{(freq_t[500]+freq_t[501])/2}")

for i in range (0, len(stat_mode)):
    file.write(f"\t\t{stat_mode[i][0]}\t {stat_mode[i][1]}\n\t\t")

print('=============STATISTICS: ==============\n=======================================\nMean:\tMedian:\t\tMode:\t Mode Count:')

if len(stat_mode) == 1:
    print(f"{mean}\t{(freq_t[500]+freq_t[501])/2}\t\t{stat_mode[i][0]}\t {stat_mode[i][1]}")
else:
    print(f"{mean}\t{(freq_t[500]+freq_t[501])/2}\t\t{stat_mode[0][0]}\t {stat_mode[0][1]}")
    for i in range (1, len(stat_mode)):
        print(f"\t\t\t{stat_mode[i][0]}\t {stat_mode[i][1]}")

file.close()