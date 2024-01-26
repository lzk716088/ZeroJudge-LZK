def t(s):
    return int(s[-1])
def num(s):
    return int(s[0])
grades = []

for _ in range(int(input())):
    data = input().split()
    total = 0
    for i in range(2,7):
        total+=int(data[i])
    data.append(str(total))
    grades.append(data)
grades.sort(key=num)
grades.sort(key=t,reverse=True)

rank=1
grades[0].append("1")
for i in range(1,len(grades)):
    rank+=1
    if grades[i][7] == grades[i-1][7]:
        grades[i].append(grades[i-1][8])
    else:
        grades[i].append(str(rank))
for i in grades:
    print(" ".join(i))
