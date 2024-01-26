people =int(input())
data = input().split()
intdata = [int(x) for x in data]
absdata = [abs(x) for x in intdata]
absdata.sort()

for i in data:
    if "-" in i:
        absdata[absdata.index(abs(int(i)))]*=-1
strdata = [str(x) for x in absdata]
p=""
for i in strdata:
    if "-" in i:
        p+="-"
    else:
        p+="o"
count = 0
for i in range(len(p)):
    if i>0 and i<len(p)-1:
        if p[i] == "o":
            if p[i-1] =="-" : count+=1
            if p[i+1] =="-" : count+=1
    elif i==0 and p[i] == "o":
            if p[i+1] =="-" : count+=1
    elif i==len(p)-1 and p[i] == "o":
            if p[i-1] =="-" : count+=1

print(count)