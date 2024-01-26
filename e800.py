N=int(input())
d=[]
def sortV(s):
    return s[1]

for _ in range(N):
    data = input().split()
    V = int(data[1])*(int(data[3])/int(data[2]))*int(data[4])
    d.append([data[0],V])
d.sort(key=sortV,reverse=True)
for i in d: i[0]
