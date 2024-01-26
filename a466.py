def ischr(c,ch):
    count=0
    for i in range(3):
        if ch[i]==c[i]:
            count+=1
    if count>=2:
        return True
    else:
        return False

for _ in range(int(input())):
    data = input()
    if len(data) == 5:
        print(3)
    elif ischr(data,"one"):
        print(1)
    elif ischr(data,"two"):
        print(2)

