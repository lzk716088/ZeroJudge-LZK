N = int(input())

data = input().split()
data = sorted([int(s) for s in data])
strdata = [str(s) for s in data]
print(" ".join(strdata))

luck=-1
unluck=101
for i in data:
    if i<60:
        luck = max(luck,i)
    else:
        unluck = min(unluck,i)
if luck <0:
    print("best case")
else:
    print(luck)
if unluck > 100:
    print("worst case")
else:
    print(unluck)
