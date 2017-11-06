r = open("./machine.inp", 'r')
line = r.readline()
info = map(int, line.split())
day = info[1]
machine = info[2]

temp = []
for j in range(0, day):
    temp.append([0, 0, 0])

profit = []
for i in range(0, machine):
    profit.append(temp[:])

lines = r.readlines()
tasks = []
for l in lines:
    s_to_i = map(int, l.split())
    s_to_i.append(0)
    tasks.append(s_to_i)

tasks.sort()
tasks.reverse()

done = day * machine
count = 0

for t in tasks:
    if count < done:
        flag = 0
        for i in range(t[1]-1, -1, -1):
            if flag:
                break
            else:
                if i < day:
                    for j in range(0, machine):
                        if profit[j][i] == [0, 0, 0]:
                            profit[j][i] = t
                            flag = 1
                            count += 1
                            t[2] = 1
                            break
    else:
        break

best = 0
for p in profit:
    best += sum(i for i, j, k in p)

# print(profit)

for i in range(0, day):
    flag = 0
    for t in tasks:
        if t[2] != 1 and t[1] > i:
            if profit[machine-1][i][0] != t[0]:
                temp[i] = best - profit[machine-1][i][0] + t[0]
                flag = 1
                break
    if flag == 0:
        if profit[machine-1][i][0] == 0:
            for m in range(machine-1, -1, -1):
                if profit[m][i][0] != 0:
                    temp[i] = best - profit[m][i][0]
                    flag = 1
                    break
            if flag == 0:
                temp[i] = best - 9999
        else:
            temp[i] = best - profit[machine-1][i][0]

second = max(temp)
# print(temp)
# print(best, second)

w = open("./machine.out", 'w')
w.write(str(best) + " " + str(second))
w.close()
