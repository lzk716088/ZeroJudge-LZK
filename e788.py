def sortbynum(s):
    return s[1]
def sortbychr(s):
    return s[0]
lst=[]
for _ in range(int(input())):
    data = input().split()
    lst.append([data[0][-1],int(data[0][0]),data[1] ])
lst.sort(key=sortbynum)
lst.sort(key=sortbychr)
for i in lst:
    print(f"{i[0]}: {i[2]}")