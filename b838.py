n=int(input())
for i in range(n):
    data = input()
    data = [a for a in data]
    L=R=0

    for i in range(len(data)):
        if data[i] =="(" : 
            L+=1
        elif data[i] ==" ":
            pass
        else:
            R+=1
        if R>L :
            print(0)
            break
        if i == len(data)-1:
            if L==R:
                print(len(data)//2)
            else:
                print(0)